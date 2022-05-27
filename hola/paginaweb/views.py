from django import dispatch
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
class index(TemplateView):
    template_name = 'index.html'

class ubuntu(TemplateView):
    template_name = 'ubuntu.html'

class docker(TemplateView):
    template_name = 'docker.html'


