from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Advertisement
from .forms import AddAdvertisementForm, EditAdvertForm
from .filters import Filters
from django.urls import reverse_lazy
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

class DeleteAdvert(DeleteView):
    model = Advertisement
    template_name = 'delete_advert.html'
    success_url = reverse_lazy('home')

class UpdateAdvert(UpdateView):
    model = Advertisement
    form_class = EditAdvertForm
    template_name = 'update_advert.html'