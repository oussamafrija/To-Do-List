from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name="list"),
    path('update-task/<int:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<int:pk>/', views.deleteTask, name="delete-task"),
]