from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Advertisement
from .forms import AddAdvertisementForm, EditAdvertForm
from .filters import Filters
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
def LovesView(request, pk):
    advertisement = get_object_or_404(Advertisement, id=request.POST.get('advertisement_id'))
    love = False
    if advertisement.loves.filter(id=request.user.id).exists():
        advertisement.loves.remove(request.user)
        love = False
    else:  
        advertisement.loves.add(request.user)
        love = True
    return HttpResponseRedirect(reverse("show_item", args=[str(pk)]))

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

    def get_context_data(self, *args, **kwargs):
        context = super(Item, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Advertisement, id=self.kwargs['pk'])
        love = False
        if stuff.loves.filter(id=self.request.user.id).exists():
            love = True
        context["love"] = love
        return context

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

class FavoriteAdvert(ListView):
    model = Advertisement
    template_name = 'favoriteadvert.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #choose adverts which user loves
        favoriteadvert = Advertisement.objects.filter(loves__exact=self.kwargs['pk'])
        context['favoriteadvert'] = favoriteadvert
        return context