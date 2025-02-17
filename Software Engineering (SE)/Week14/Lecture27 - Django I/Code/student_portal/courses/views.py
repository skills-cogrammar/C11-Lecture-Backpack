# courses/views.py

from django.shortcuts import render
# Create your views here.


# View that Renders a Template
def home(request):
    return render(request, "courses/home.html")


# View That Sends Data to a Template
def courses_list(request):
    courses = ["Maths", "Science", "History", "Computer Science"]
    return render(request, "courses/courses_list.html", {"courses": courses})
