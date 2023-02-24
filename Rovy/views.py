from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Home.html')
def cv(request):
    return render(request, 'cv.html')   
def hireme(request):
    return render(request, 'hire-me.html') 
def projects(request):
    return render(request, 'projects.html')
