from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Todo
from django.conf import settings

@shared_task
def send_due_date_reminder():
    one_hour_from_now = timezone.now() + timedelta(hours=1)
    todos = Todo.objects.filter(due_date__gte=one_hour_from_now, due_date__lt=one_hour_from_now + timedelta(minutes=1))
    
    for todo in todos:
        send_mail(
            subject='Reminder: Task Due in 1 Hour',
            message=f'Your task "{todo.title}" is due in 1 hour.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[todo.owner.email],
            fail_silently=False,
        )

    return f"Sent {len(todos)} reminders"