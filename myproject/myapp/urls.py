from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('task/delete/<int:task_id>', views.delete_task_view, name='delete_task'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('task/new', views.create_task_view, name='new_task'),
    path('register', views.register_view, name='register'),
]
