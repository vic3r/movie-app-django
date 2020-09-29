from django.test import TestCase
from datetime import date
from .models import Actor, Film, Director

class ActorTestCase(TestCase):
    def setUp(self):
        Actor.objects.create(name='Saoirse', last_name='Ronan', birthdate=date(1994 , 4 , 12), country='USA')
        Actor.objects.create(name='Rami', last_name='Malek', birthdate=date(1981 , 5 , 12), country='USA')
    
    def test_get_all_actors(self):
        total_actors = Actor.objects.all()
        self.assertEqual(len(total_actors), 2)

    def test_get_actor_age(self):
        rami = Actor.objects.get(name='Rami')
        saoirse = Actor.objects.get(name='Saoirse')
        self.assertEqual(rami.age, 39)
        self.assertEqual(saoirse.age, 26)

class DirectorTestCase(TestCase):
    def setUp(self):
        Director.objects.create(name='Greta', last_name='Gerwig', birthdate=date(1983 , 8 , 4), country='USA')

    def test_get_directors(self):
        total_directors = Director.objects.all()
        self.assertEqual(len(total_directors), 1)
    
    def test_get_actor_age(self):
        greta = Director.objects.get(name='Greta')
        self.assertEqual(greta.age, 37)


class FilmTestCase(TestCase):
    def setUp(self):
        saoirse = Actor.objects.create(name='Saoirse', last_name='Ronan', birthdate=date(1994 , 4 , 12), country='USA')
        film_instance = Film.objects.create(title='Lady Bird', duration='94 minutes', year=2017, genre='Drama', price=50.00)
        film_instance.actors.add(saoirse)
    
    def test_get_movies(self):
        total_films = Film.objects.all()
        self.assertEqual(len(total_films), 1)
    
