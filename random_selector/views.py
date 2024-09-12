from django.shortcuts import render, redirect
import random

students = ["Griqor", "Ani", "Arianna", "Suren"]

def select_random_student(request):
    selected_student = random.choice(students)
    return render(request, 'selector/select.html', {'selected_student': selected_student, 'students': students})

def add_student(request):
    if request.method == 'POST':
        student_name = request.POST['student_name'].strip()  # Strip whitespace
        if student_name in students:
            # If the student already exists, show an error message
            error_message = f"{student_name} is already in the list."
            return render(request, 'selector/select.html', {
                'students': students,
                'error_message': error_message,
                'selected_student': random.choice(students)  # Randomly select a student
            })
        else:
            # Add the student if it doesn't exist
            students.append(student_name)
            return redirect('select_random_student')

def group_students(request):
    if request.method == 'POST':
        group_size = int(request.POST['group_size'])
        random.shuffle(students)
        groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
        return render(request, 'selector/groups.html', {'groups': groups})
    return redirect('select_random_student')
