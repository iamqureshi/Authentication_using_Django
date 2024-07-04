from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('list/', views.get_student_list, name='student_list'),
    path('update/', views.update_student, name='update_student'),
    path('add/', views.create_student, name='add_student'),
    path('delete/', views.delete_student, name='delete_student'),
]