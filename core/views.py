from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, WorkExperience,Education, Skill, Hobby, Contact
# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Homepage'})

def cv(request):
    context = {
        'title': 'CV',
        'education': Education.objects.all(),
        'works': WorkExperience.objects.all(),
        'skills': Skill.objects.all(),
        'hobbies': Hobby.objects.all(),
    }
    return render(request, 'cv.html', context)

def hireme(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, f'Your message has been sent succesfully!')
        return redirect('index')
    return render(request, 'hire-me.html', {'title': 'Hire Me'})

def projects(request):
    context = {
        'title': 'Projects',
        'projects': Project.objects.all()
    }
    return render(request, 'projects.html', context)