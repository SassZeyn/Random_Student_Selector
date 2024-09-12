from django.urls import path
from . import views  # Import from the current app

urlpatterns = [
    path('', views.select_random_student, name='select_random_student'),  # The main view
    path('add-student/', views.add_student, name='add_student'),          # URL to add students
    path('group-students/', views.group_students, name='group_students'),  # URL for grouping students
]
