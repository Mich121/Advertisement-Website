from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#class which decribe our advertisements
class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=600)
    price = models.FloatField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.owner)
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')