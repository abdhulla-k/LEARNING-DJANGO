from rest_framework import serializers
from .models import MoviesData

# using model serializer
class ModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = MoviesData
        fields = [ 'id', 'name', 'duration', 'rating', 'typ']