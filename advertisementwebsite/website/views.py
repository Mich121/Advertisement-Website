from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Advertisement
from .forms import AddAdvertisementForm
from .filters import Filters
# Create your views here.
class HomeView(ListView):
    model = Advertisement
    template_name = 'home.html'
    ordering = ['-post_date']

    #filter data by title of advertisement in search bar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Filters(self.request.GET, queryset=self.get_queryset())
        return context

class Item(DetailView):
    model = Advertisement
    template_name = 'show_item.html'

class AddAdvertisement(CreateView):
    model = Advertisement
    form_class = AddAdvertisementForm
    template_name = 'add_advertisement.html'