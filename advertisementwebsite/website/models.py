from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class which decribe our advertisements
class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    #header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.owner)