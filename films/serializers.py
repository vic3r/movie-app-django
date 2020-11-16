from rest_framework import serializers
from .models import Person, Movie

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'imdb_name_id',
            'name',
            'birth_name',
            'height',
            'bio',
            'birth_details',
            'date_of_birth',
            'place_of_birth',
            'death_details',
            'date_of_death',
            'place_of_death',
            'reason_of_death',
            'spouses_string',
            'spouses',
            'divorces',
            'spouses_with_children',
            'children',
        )
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'imdb_title_id',
            'title',
            'original_title',
            'year',
            'date_published',
            'genre',
            'duration',
            'country',
            'language',
            'director',
            'writer',
            'production_company',
            'actors',
            'description',
            'avg_vote',
            'votes',
            'budget',
            'usa_gross_income',
            'worldwide_gross_income',
            'metascore',
            'reviews_from_users',
            'reviews_from_critics',
            'image'
        )
