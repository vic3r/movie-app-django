from django.urls import include

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('new-films', views.FilmView)
router.register('actors', views.ActorView)
router.register('directors', views.DirectorView)

urlpatterns = [
    path('', include(router.urls))
]