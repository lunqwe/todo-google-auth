from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from .models import Todo  # Adjust this import based on your app structure
from .serializers import CreateTodoSerializer  # Adjust this import based on your serializer

class CreateTodoViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('create_todo')

    def test_create_todo(self):
        data = {
            'title': 'Test Todo',
            'description': 'This is a test todo item',
            'due_date': '2024-07-15T12:00:00Z'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        todo = Todo.objects.get(title='Test Todo')
        self.assertEqual(todo.description, 'This is a test todo item')

    def test_create_todo_unauthenticated(self):
        self.client.logout()
        data = {
            'title': 'Test Todo',
            'description': 'This is a test todo item',
            'due_date': '2024-07-15T12:00:00Z'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
class RetrieveTodoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@gmail.com')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword', email='test2@gmail.com')
        self.todo = Todo.objects.create(title='Test Todo', description='Test description', owner=self.user, due_date='2024-09-09:14-00')

    def test_retrieve_own_todo(self):
        # as owner
        self.client.force_authenticate(user=self.user)
        url = reverse('retrieve-todo', kwargs={'pk': self.todo.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Todo')
        self.assertEqual(response.data['owner'], self.user.id)

    def test_retrieve_other_user_todo(self):
        # as not owner
        self.client.force_authenticate(user=self.other_user)
        url = reverse('retrieve-todo', kwargs={'pk': self.todo.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_unauthenticated(self):
        # without auth
        url = reverse('retrieve-todo', kwargs={'pk': self.todo.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_invalid_pk(self):
        # invalid todo pk
        self.client.force_authenticate(user=self.user)
        url = reverse('retrieve-todo', kwargs={'pk': 999})  # предполагая, что pk 999 не существует
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TodoListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@gmail.com')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword', email='test2@gmail.com')
        self.todo1 = Todo.objects.create(title='Test Todo 1', description='Test description 1', owner=self.user, due_date='2024-09-09:14-00')
        self.todo2 = Todo.objects.create(title='Test Todo 2', description='Test description 2', owner=self.user, due_date='2024-09-09:14-00')
        self.todo3 = Todo.objects.create(title='Test Todo 3', description='Test description 3', owner=self.other_user, due_date='2024-09-09:14-00')

    def test_list_own_todos(self):
        # todo list (only own)
        self.client.force_authenticate(user=self.user)
        url = reverse('list-todo-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 2)  
        
    def test_list_unauthenticated(self):
        url = reverse('list-todo-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_by_due_date(self):
        # filtering by due date
        self.client.force_authenticate(user=self.user)
        url = reverse('list-todo-view')
        filter_params = {'due_date': '2024-07-31:14-00'}
        response = self.client.get(url, filter_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 0)


class UpdateTodoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='testuser', password='testpassword', email='test@gmail.com')
        self.user2 = User.objects.create_user(username='otheruser', password='otherpassword', email='test2@gmail.com')

        self.todo1 = Todo.objects.create(title='Test Todo 1', description='Test description 1', owner=self.user1, due_date='2024-09-09:14-00')
        self.todo2 = Todo.objects.create(title='Test Todo 2', description='Test description 2', owner=self.user2, due_date='2024-09-09:14-00')

    def test_update_own_todo(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('update-todo-view', kwargs={'pk': self.todo1.pk})
        data = {'title': 'Updated Test Todo 1', 'description': 'Updated description 1', 'owner':1, 'due_date': '2024-09-09:14-00'}
        response = self.client.put(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated Test Todo 1')
        self.assertEqual(self.todo1.description, 'Updated description 1')

    def test_update_other_user_todo(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('update-todo-view', kwargs={'pk': self.todo2.pk})
        data = {'title': 'Updated Test Todo 2', 'description': 'Updated description 2'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)