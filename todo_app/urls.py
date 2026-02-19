from django.urls import path
from todo_app import views

urlpatterns = [
    path('add_task/',views.add_task,name='add_task')
]
