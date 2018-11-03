from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def aboutme(request):
    return render(request,'durgasoft_aboutme.html')
def aboutpython(request):
    return render(request,'durgasoft_aboutpython.html')
def aboutdjango(request):
    return render(request,'durgasoft_aboutdjango.html')
def aboutcourses(request):
    return render(request,'durgasoft_courses.html')

