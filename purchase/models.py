from django.db import models
from authentication.models import UserProfile
from films.models import Movie

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=255, null=False),
    last_name = models.CharField(max_length=255, null=False),
    number = models.IntegerField(null=False),
    user = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT),

    class Meta:
        db_table = 'card'

class Purchase(models.Model):
    id = models.AutoField(primary_key=True),
    amount = models.FloatField()
    user = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT),
    card = models.ForeignKey(
        Card, on_delete=models.PROTECT),
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT),

    class Meta:
        db_table = 'purchase'
