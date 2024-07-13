from django.urls import path

from .views import CreateTodoView, RetrieveTodoView, TodoListView, UpdateTodoView, DeleteTodoView

urlpatterns = [
    path('create/', CreateTodoView.as_view(), name='create_todo'),
    path('get/<int:pk>', RetrieveTodoView.as_view(), name='retrieve-todo'),
    path('list/', TodoListView.as_view(), name='list-todo-view'),
    path('update/<int:pk>', UpdateTodoView.as_view(), name='update-todo-view'),
    path('delete/<int:pk', DeleteTodoView.as_view(), name='delete-todo-view'),
]
