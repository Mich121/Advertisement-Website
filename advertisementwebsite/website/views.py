from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Advertisement
from .forms import AddAdvertisementForm
# Create your views here.
class HomeView(ListView):
    model = Advertisement
    template_name = 'home.html'
    ordering = ['-post_date']

class Item(DetailView):
    model = Advertisement
    template_name = 'show_item.html'

class AddAdvertisement(CreateView):
    model = Advertisement
    form_class = AddAdvertisementForm
    template_name = 'add_advertisement.html'