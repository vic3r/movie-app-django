from django.test import TestCase
from datetime import date
from .models import Person, Movie

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            imdb_name_id='t001',
            name='Saoirse Ronan',
            birth_name='',
            height=178,
            bio='',
            birth_details='',
            date_of_birth='1994, 4, 12',
            place_of_birth='Queens, New York, NY, USA',
            death_details='',
            date_of_death='',
            place_of_death='',
            reason_of_death='',
            spouses_string='',
            spouses=0,
            divorces=0,
            spouses_with_children=0,
            children=0,
        )    
        Person.objects.create(
            imdb_name_id='t002',
            name='Rami Malek',
            birth_name='',
            height=175,
            bio='',
            birth_details='',
            date_of_birth='1981, 9, 11',
            death_details='',
            place_of_birth='Queens, New York, NY, USA',
            date_of_death='',
            place_of_death='',
            reason_of_death='',
            spouses_string='',
            spouses=1,
            divorces=0,
            spouses_with_children=0,
            children=2,
        )
    
    def test_get_all_actors(self):
        total_actors = Person.objects.all()
        self.assertEqual(len(total_actors), 2)

    def test_get_actor_spouses(self):
        rami = Person.objects.get(name='Rami Malek')
        saoirse = Person.objects.get(name='Saoirse Ronan')
        self.assertEqual(rami.spouses, 1)
        self.assertEqual(saoirse.spouses, 0)

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(
            imdb_title_id="t001",
            title='Lady Bird',
            original_title="",
            year='2017-08-05',
            date_published="",
            genre="Drama",
            duration=94,
            country="",
            language="",
            director="",
            writer="",
            production_company="",
            actors="",
            description="",
            avg_vote=8.1,
            votes=230000,
            budget="",
            usa_gross_income="",
            worldwide_gross_income="",
            metascore=8.8,
            reviews_from_users=7.6,
            reviews_from_critics=8.2,
        )
    
    def test_get_movies(self):
        total_movies = Movie.objects.all()
        self.assertEqual(len(total_movies), 1)
    
    def test_get_movie_votes(self):
        lady_bird = Movie.objects.get(title='Lady Bird')
        self.assertEqual(lady_bird.votes, 230000)
