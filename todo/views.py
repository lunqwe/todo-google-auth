from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.state import token_backend
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from django_filters.rest_framework import DjangoFilterBackend


from .models import Todo
from .serializers import CreateTodoSerializer, TodoSerializer
from .permissions import IsOwner
from .filters import TodoFilter
from accounts.models import User

def test_goole_auth(request):
    return render(request, 'test.html')


class CreateTodoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateTodoSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        try:
            user = User.objects.get(id=self.request.user.id)
            serializer.save(owner=user)
            
        except InvalidToken:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

    
class RetrieveTodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_field = 'pk'

    
class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter
    
class UpdateTodoView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_field = 'pk'
    

class DeleteTodoView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_field = 'pk'
    
    

    
    
    