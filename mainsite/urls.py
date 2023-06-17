from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('weather/', views.weather_app, name='weather'),
    path('login/', views.login_page, name='login'),
    path('register/',views.register_page, name='register'),
    path('tasks/', views.task_page, name='tasks'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # path('budget/', views.budget_page, name='budget'),
    # path('budget/<str:budget_id>/', views.delete_budget, name='delete_budget_item'),

]
