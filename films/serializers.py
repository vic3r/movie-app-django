from rest_framework import serializers
from .models import Actor, Film, Director

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor

        fields = ['id', 'name', 'last_name', 'birthdate', 'country', 'img_url']
class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'duration', 'genre', 'actors', 'price', 'img_url', 'video_url']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'last_name', 'birthday', 'films', 'country', 'img_url']