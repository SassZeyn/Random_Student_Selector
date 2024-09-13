from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_random_student, name='select_random_student'),  # The main view
    path('add-student/', views.add_student, name='add_student'),  # Add student URL
    path('delete-student/<str:student_name>/', views.delete_student, name='delete_student'),  # Delete student URL
    path('group-students/', views.group_students, name='group_students'),  # Group students URL
]
