from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advertisement
# Create your views here.
class HomeView(ListView):
    model = Advertisement
    template_name = 'home.html'
    ordering = ['-post_date']

class Item(DetailView):
    model = Advertisement
    template_name = 'item.html'