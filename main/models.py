from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Doctors(models.Model):
    title = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=200)
    desc = RichTextField(blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='upload', blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

