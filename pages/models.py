from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    adminlar = (
        ("Shahzod","Shahzod"),
        ("Anvar", "Anvar"),
        ("Qobil", "Qobil"),
        ("Davron","Davron"),
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    summery = models.CharField(max_length=200)
    photo = models.ImageField(upload_to= 'images/')
    data = models.DateTimeField()
    admin = models.CharField(max_length = 10, choices= adminlar)
    
    def __str__(self):
        return self.title

class Murojatlar(models.Model):
    ism = models.CharField(max_length=15)
    familya = models.CharField(max_length=25)
    tel_raqam = models.PositiveIntegerField(max_length=9)
    murojatlar = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.murojatlar
    
    def get_absolute_url(self):
        return reverse('contact')