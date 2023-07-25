from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Tasks


class HomePage(ListView):
    model = Tasks
    template_name = 'todo/home_page.html'
