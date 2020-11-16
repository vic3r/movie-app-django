from django.shortcuts import render
from rest_framework import viewsets, mixins
from purchase.models import Purchase, Card
from purchase.serializers import PurchaseSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authentication import permissions

# Create your views here.

class PurchaseView(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)

class CardView(mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)

