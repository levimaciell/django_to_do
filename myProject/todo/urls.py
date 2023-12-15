from . import views
from django.urls import path

urlpatterns = [
    path('todo', views.todo_endpoint, name = 'todo(get, post)'),
    path('todo/<int:id>', views.todo_endpoint_id, name = 'todo(update, delete)')
]