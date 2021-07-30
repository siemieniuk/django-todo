from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('task/delete/<int:task_id>',
         views.task_delete_view, name='delete_task'),
    path('task/new', views.task_create_view, name='new_task'),
    path('register', views.register_view, name='register'),
]
