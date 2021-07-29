from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('delete-task/<int:id>', views.delete_task_view, name='deletetask'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('new-task', views.create_task_view, name='newtask'),
    path('register', views.register_view, name='register'),
]
