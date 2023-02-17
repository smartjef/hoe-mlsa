from django.shortcuts import render
from .models import Project, WorkExperience,Education
# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Homepage'})

def cv(request):
    context = {
        'title': 'CV',
        'education': Education.objects.all(),
        'works': WorkExperience.objects.all()
    }
    return render(request, 'cv.html', context)

def hireme(request):
    return render(request, 'hire-me.html')

def projects(request):
    context = {
        'title': 'Projects',
        'projects': Project.objects.all()
    }
    return render(request, 'projects.html', context)