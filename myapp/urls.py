from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="show_tasks"),
    path('projects/', views.Projects, name="projects"),
    path('forms/', views.Forms, name="create_task"),
    path('prj_form/', views.projects_form, name="create_project"),
    path('delete_task/<int:id_task>/', views.delete_task, name="delete_task"),
    path('done_tasks/<int:id_task>/', views.done_tasks, name="done_tasks"),
    path('delete_projects/<int:id_project>/', views.delete_projects, name="delete_projects"),
    path('done_projects/<int:id_projects>/', views.done_projects, name="done_projects")
]
