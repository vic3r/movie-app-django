from rest_framework import serializers
from purchase import models

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('name', 'last_name', 'number', 'user_id')
        
        def create(self, validated_data):
            card = models.Card.objects.create(
                name=validated_data['name'],
                last_name=validated_data['last_name'],
                number=validated_data['number'],
                user_id=validated_data['user_id'],
            )

            return card

        def update(self, instance, validated_data):
            if 'number' in validated_data:
                number = validated_data.pop('number')
                instance.set_number(number)

            return super().update(instance, validated_data)

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('user_id', 'card_id', 'amount', 'movie_id')

        def create(self, validated_data):
            purchase = models.Purchase.objects.create(
                user_id=validated_data['user_id'],
                card_id=validated_data['card_id'],
                amount=validated_data['amount'],
                movie_id=validated_data['movie_id'],
            )

            return purchase
