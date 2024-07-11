from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import CreateTodoSerializer, TodoSerializer
from .permissions import IsOwner



class CreateTodoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateTodoSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    