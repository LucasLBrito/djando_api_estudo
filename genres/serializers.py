from rest_framework import serializers
from genres.models import Genre

class GenreSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'