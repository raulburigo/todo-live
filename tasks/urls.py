from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklist, name='task-list'),
    path('tasks/<int:task_id>', views.taskdetail, name='task-detail'),
    path('edit/<int:task_id>', views.taskedit, name='task-edit'),
    path('delete/<int:task_id>', views.taskdelete, name='task-delete'),
    path('done/<int:task_id>', views.taskdone, name='task-done'),
    path('newtask/', views.newtask, name='new-task'),
    path('boots/', views.bootsview, name='boots'),
]
