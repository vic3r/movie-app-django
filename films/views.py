import requests
from django.shortcuts import render
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from .models import Actor, Film, Director
from .serializers import ActorSerializer, FilmSerializer, DirectorSerializer

url = "https://imdb8.p.rapidapi.com/title"
headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': 'API_KEY'
}

def fetch_soon_movies():
    querystring = {"homeCountry": "US","purchaseCountry": "US","currentCountry": "US"}
    try:
        soon_movies = requests.request("GET", f'{url}/get-coming-soon-movies', headers=headers, params=querystring)
        for title in soon_movies.json()[:3]:
            title_id = title.split('/')[-2]
            fetch_movie_details(title_id)
    except Exception:
        raise HttpResponseServerError

def fetch_movie_details(title_id):
    try:
        querystring = {"tconst":"tt8784956"}
        movie_details = requests.request("GET", f'{url}/get-details', headers=headers, params=querystring)
        movie_details = movie_details.json()
        Film.objects.create(
            title=movie_details['title'],
            duration=movie_details['runningTimeInMinutes'],
            genre=movie_details['titleType'],
            year=movie_details['year'],
            price=50.00,
            img_url=movie_details['image']['url'],
        )
    except Exception as e:
        print(e)
        raise HttpResponseServerError

fetch_soon_movies()

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class DirectorView(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
