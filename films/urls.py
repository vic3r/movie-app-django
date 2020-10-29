from django.urls import include

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.MovieView, basename='movies')
router.register('persons', views.PersonView)

urlpatterns = [
    path('', include(router.urls))
]