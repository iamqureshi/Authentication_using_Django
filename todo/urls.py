from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.todo_list),
    path('list/<int:pk>/', views.todo_detail),
]
