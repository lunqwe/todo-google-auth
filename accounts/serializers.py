from rest_framework import serializers
from dj_rest_auth.serializers import PasswordResetSerializer as DefaultPasswordResetSerializer
from django.conf import settings

from .models import User

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, data: dict):
        password = data.get('password')
        password2 = data.get('password2')
        
        if password == password2:
            data.pop('password2')
            return data
        else:
            raise serializers.ValidationError('Passwords didn`t match.')
    
class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email is not registered.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Wrong password.")
        
        data['user'] = user
        return data
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email'] # TODO: add fields after all user variables are known     
        
        
class GoogleAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField()
    
    
class PasswordResetSerializer(DefaultPasswordResetSerializer):
    def get_email_options(self):
        return {
            'domain_override': settings.DOMAIN,
            'email_template_name': settings.EMAIL_TEMPLATE_NAME,
            'extra_email_context': {
                'site_name': settings.SITE_NAME,
            },
        }

        
        
    
    
    
