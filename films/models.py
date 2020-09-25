from django.db import models
from datetime import date 

class Actor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField()
    country = models.CharField(max_length=100)
    img_url = models.URLField()
    
    def get_age(self) -> int:
        today = date.today()
        age = (today.year - self.birthdate.year -
            ((today.month, today.day) < (self.birthdate.month, self.birthdate.day)))
        return age
    
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    genre = models.CharField(max_length=40)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    price = models.DecimalField(decimal_places=2, default=0.0, max_digits=5)
    img_url = models.URLField()
    video_url = models.URLField()
    
    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField()
    films = models.ManyToManyField(Film)
    country = models.CharField(max_length=40)
    img_url = models.URLField()

    def get_age(self) -> int:
        today = date.today()
        age = (today.year - self.birthdate.year -
            ((today.month, today.day) < (self.birthdate.month, self.birthdate.day)))
        return age
    
    def __str__(self):
        return self.name
