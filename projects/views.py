from django.shortcuts import render
from .models import Projects

# Create your views here.
def homepage(request):
    projects = Projects.objects
    return render(request,'projects/home.html',{"projects":projects})