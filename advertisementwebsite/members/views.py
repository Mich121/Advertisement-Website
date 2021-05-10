from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import RegisterForm, ProfilePageForm
from django.urls import reverse_lazy
from website.models import Profile, Advertisement

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

class UpdateProfile(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/update_profile_page.html'
    #fields = ['name', 'surname', 'profile_picture', 'phone', 'email', 'city']
    success_url = reverse_lazy('home')

class CreateProfile(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfile(generic.DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfile, self).get_context_data(*args, **kwargs)
        #choose correct user
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        #choose adverts of user
        user_adverts = Advertisement.objects.filter(owner=page_user.user)
        print(user_adverts)
        context["page_user"] = page_user
        context["user_adverts"] = user_adverts
        return context