from django.shortcuts import render, redirect
import random

# List of students
students = ["Griqor", "Ani", "Arianna", "Suren"]

# Variable to store the last selected student
last_selected_student = None

def select_random_student(request):
    global last_selected_student  # Access the global variable
    if students:  # Check if the list is not empty
        if len(students) == 1:  # If only one student, select that one
            selected_student = students[0]
        else:
            # Keep selecting a random student until it's not the same as the last one
            selected_student = random.choice(students)
            while selected_student == last_selected_student:
                selected_student = random.choice(students)
        last_selected_student = selected_student  # Update the last selected student
    else:
        selected_student = "No students available"
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
                'selected_student': random.choice(students) if students else "No students available"  # Handle empty case
            })
        else:
            # Add the student if it doesn't exist
            students.append(student_name)
            return redirect('select_random_student')

def delete_student(request, student_name):
    global last_selected_student  # Access the global variable
    # Check if the student is in the list and remove it
    if student_name in students:
        students.remove(student_name)
        # Reset last selected student if it was deleted
        if last_selected_student == student_name:
            last_selected_student = None
    return redirect('select_random_student')

def group_students(request):
    if request.method == 'POST':
        group_size = int(request.POST['group_size'])
        if group_size > 0 and len(students) >= group_size:
            random.shuffle(students)  # Shuffle the list of students randomly
            # Create groups by slicing the shuffled student list
            groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
            return render(request, 'selector/groups.html', {'groups': groups})
        else:
            error_message = "Group size must be smaller than or equal to the number of students."
            return render(request, 'selector/select.html', {
                'students': students,
                'error_message': error_message,
                'selected_student': random.choice(students) if students else "No students available"
            })
    return redirect('select_random_student')
