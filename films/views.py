import requests
from rest_framework import viewsets, mixins
from .models import Person, Movie
from .serializers import PersonSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from http import HTTPStatus

from authentication import permissions
from authentication.models import UserProfile
from contactsapi import settings
import requests

class MovieView(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)

    def get_image(self,  obj):
        title_id = obj.imdb_title_id
        image_gateway_uri = f'http://{settings.IMAGE_GATEWAY_HOST}:{settings.IMAGE_GAYEWAY_PORT}/images/movies/{title_id}'
        response = requests.get(image_gateway_uri)
        image = response.json()
        obj.image = image['value']

        return obj

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
        result = [self.get_image(q) for q in queryset.iterator()]
        return result

class MovieUserView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
            
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)

    def get_queryset(self):
        queryset = Movie.objects.all()
        email = self.request.query_params.get('email')
        if email:
            user = UserProfile.objects.get(email=email)
            queryset = queryset.filter(users=user)
            return queryset
        else:
            return Response({'msg': f'email not found'}, HTTPStatus.BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        if 'email' not in request.data:
            return Response({'msg': f'email not found'}, HTTPStatus.BAD_REQUEST)
        if 'movie_id' not in request.data:
            return Response({'msg': f'movie_id not found'}, HTTPStatus.BAD_REQUEST)
        email = request.data['email']
        movie_id = request.data['movie_id']
        movie = queryset.get(id=movie_id)
        user = UserProfile.objects.get(email=email)
        if not movie or not user:
            return Response({'msg': f'user/movie {movie_id} not found'}, HTTPStatus.NOT_FOUND)
        movie.users.add(user)
        movie.save()
        return Response({'msg': f'movie {movie_id} added'}, HTTPStatus.CREATED)

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
