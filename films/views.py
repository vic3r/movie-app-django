import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from rest_framework.response import Response
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
        if title:
            queryset = queryset.filter(title=title)
        elif genre:
            queryset = queryset.filter(genre=genre)
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
            queryset = queryset.filter(name=name)
        return queryset
