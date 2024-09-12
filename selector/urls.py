from django.urls import path
from random_selector import views

urlpatterns = [
    path('', views.select_random_student, name='select_random_student'),  # The main view
    path('add-student/', views.add_student, name='add_student'),  # Add student URL
    path('test/', views.test_view, name='test_view'),
]
