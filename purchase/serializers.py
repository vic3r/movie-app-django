from rest_framework import serializers
from purchase import models

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('name', 'last_name', 'number', 'user')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('user', 'card', 'amount', 'movie')
