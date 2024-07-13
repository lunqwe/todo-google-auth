from datetime import timezone
from rest_framework import serializers

from .models import Todo

class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'due_date']
        
    def create(self, validated_data):
        due_date = validated_data['due_date']
        if due_date <= timezone.now():
            raise serializers.ValidationError("The due date must be in the future.")
        return Todo.objects.create(**validated_data)
        
        
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        
        
class GoogleAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField(required=True)