This Random Student Selector is a Django-based web application designed for teachers and educators to randomly select students for classroom activities and group tasks. The tool provides an engaging, interactive, and user-friendly interface that enhances student engagement during lessons.

The application supports several key features:

Random student selection from a predefined list, ensuring no consecutive repetitions.
Ability to dynamically add or remove students from the list.
Grouping of students into random groups for group activities.
A visually appealing interface with buttons for adding, deleting, and grouping students.
All student lists are presented in a clean table format with delete buttons represented by red crosses for each student.
This application has been deployed using PythonAnywhere, and the source code is available on GitHub for easy collaboration, contributions, or personal use.

Key Features

Random Student Selector: Ensures no consecutive student is selected back to back.
Student Management: Add or delete students dynamically via a simple form.
Student Grouping: Automatically group students into random groups based on user-defined group sizes.
Interactive UI: The interface includes responsive buttons, visually appealing tables, and color-coded elements to enhance usability.
Django-powered: Built with Django, utilizing HTML and CSS for the frontend.
Deployed on PythonAnywhere: The application can be run easily in the cloud for classroom use.
Technology Stack

Python: Core language for the project.
Django: Web framework used to develop the application.
HTML/CSS: Used to create a visually appealing and responsive user interface.
PythonAnywhere: Cloud platform used for deployment.
GitHub: Version control and source code hosting.

Installation and Setup

1. Clone the repository
git clone https://github.com/your-username/random_student_selector.git
cd random_student_selector
2. Set up a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies
pip install -r requirements.txt
4. Run the application locally
python manage.py migrate
python manage.py runserver
5. Deploying on PythonAnywhere
Sign up at PythonAnywhere.
Create a new web app with Django.
Clone this GitHub repository to your PythonAnywhere Bash console:
git clone https://github.com/your-username/random_student_selector.git
cd random_student_selector
Create a virtual environment on PythonAnywhere:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Configure the WSGI file and static files to connect your app to PythonAnywhere’s web hosting.
Once configured, visit your PythonAnywhere subdomain to view and use the app.

Usage

Select a Random Student: Click the "Select Random Student" button, and a student will be randomly chosen from the list.
Add a Student: Use the input field to add a new student. Click the "Add Student" button to update the list.
Delete a Student: Click the red cross next to any student's name to remove them from the list.
Group Students: Specify the group size in the input field and click "Create Groups" to randomly divide students into groups.
Contributing

Feel free to submit issues and pull requests! Contributions are always welcome.

Deployed Version

You can view a live version of this project hosted on PythonAnywhere at: (https://sasszeyn.pythonanywhere.com)
