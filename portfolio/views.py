from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.db import models


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
