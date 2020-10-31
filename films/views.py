import requests
from rest_framework import viewsets, mixins
from .models import Person, Movie
from .serializers import PersonSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from authentication import permissions

class MovieView(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)

    def get_queryset(self):
        queryset = Movie.objects.all()
        title = self.request.query_params.get('title')
        genre = self.request.query_params.get('genre')
        actor = self.request.query_params.get('actor')
        director = self.request.query_params.get('director')
        avg_vote = self.request.query_params.get('avg_vote')
        if title:
            queryset = queryset.filter(title__contains=title)
        if genre:
            queryset = queryset.filter(genre__contains=genre)
        if actor:
            queryset = queryset.filter(actors__contains=actor)
        if director:
            queryset = queryset.filter(director__contains=director)
        if avg_vote:
            queryset = queryset.filter(avg_vote__gte=avg_vote)
        return queryset

class PersonView(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)

    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset
