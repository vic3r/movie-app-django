from django.db import models
from datetime import date 

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    imdb_name_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birth_name = models.CharField(max_length=400, null=True)
    height = models.IntegerField(null=True)
    bio = models.TextField(null=True)
    birth_details = models.CharField(max_length=400, null=True)
    date_of_birth = models.CharField(max_length=500, null=True)
    place_of_birth = models.CharField(max_length=200, null=True)
    death_details = models.TextField(null=True)
    date_of_death = models.CharField(max_length=100, null=True)
    place_of_death = models.CharField(max_length=200, null=True)
    reason_of_death = models.CharField(max_length=200, null=True)
    spouses_string = models.TextField(null=True)
    spouses = models.IntegerField(null=True)
    divorces = models.IntegerField(null=True)
    spouses_with_children = models.IntegerField(null=True)
    children = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'person'

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    imdb_title_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    year = models.CharField(max_length=100, null=True)
    date_published = models.CharField(max_length=20, null=True)
    genre = models.CharField(max_length=50, null=True)
    duration = models.IntegerField()
    country = models.CharField(max_length=500, null=True)
    language = models.CharField(max_length=500, null=True)
    director = models.CharField(max_length=100, null=True)
    writer = models.CharField(max_length=100, null=True)
    production_company = models.CharField(max_length=200, null=True)
    actors = models.TextField(null=True)
    description = models.TextField(null=True)
    avg_vote = models.FloatField(default=0.0, null=True)
    votes = models.IntegerField(null=True)
    budget = models.CharField(max_length=100, default='', null=True)
    usa_gross_income = models.CharField(max_length=100, default='', null=True)
    worldwide_gross_income = models.CharField(max_length=100, default='', null=True)
    metascore = models.FloatField(default=0.0, null=True)
    reviews_from_users = models.FloatField(default=0.0, null=True)
    reviews_from_critics = models.FloatField(default=0.0, null=True)
    image = models.TextField(default='', null=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'movie'
