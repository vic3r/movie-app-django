from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=255, null=False),
    last_name = models.CharField(max_length=255, null=False),
    number = models.IntegerField(null=False),
    user_id = models.IntegerField(null=False),

    class Meta:
        db_table = 'card'

class Purchase(models.Model):
    user_id = models.IntegerField(null=False),
    card_id = models.IntegerField(null=False),
    movie_id = models.IntegerField(null=False),
    amount = models.FloatField()

    class Meta:
        db_table = 'purchase'
