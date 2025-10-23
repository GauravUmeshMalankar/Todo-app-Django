from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
# Define URL patterns for the tasks app
# Map URLs to corresponding view functions
# what are urls in django ?
# URLs are used to map specific web addresses to corresponding view functions in Django.
# They define the routes that users can access in a web application and determine which code should be executed when a particular URL is requested.