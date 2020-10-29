from django.db import models
from datetime import date 

class Person(models.Model):
    imdb_name_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birth_name = models.CharField(max_length=400)
    height = models.IntegerField()
    bio = models.TextField()
    birth_details = models.CharField(max_length=400)
    date_of_birth = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=200)
    death_details = models.TextField()
    date_of_death = models.CharField(max_length=100)
    place_of_death = models.CharField(max_length=200)
    reason_of_death = models.CharField(max_length=200)
    spouses_string = models.TextField()
    spouses = models.IntegerField()
    divorces = models.IntegerField()
    spouses_with_children = models.IntegerField()
    children = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'person'

class Movie(models.Model):
    imdb_title_id = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    date_published = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    country = models.CharField(max_length=500)
    language = models.CharField(max_length=500)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    production_company = models.CharField(max_length=200)
    actors = models.TextField()
    description = models.TextField()
    avg_vote = models.FloatField(default=0.0)
    votes = models.IntegerField()
    budget = models.CharField(max_length=100)
    usa_gross_income = models.CharField(max_length=100, default='')
    worldwide_gross_income = models.CharField(max_length=100, default='')
    metascore = models.FloatField(default=0.0)
    reviews_from_users = models.FloatField(default=0.0)
    reviews_from_critics = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'movie'
