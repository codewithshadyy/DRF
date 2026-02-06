from .models import Artist, Song, Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = "__all__"
class ArtistSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True) 
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'genre', 'genre_name'] 
        
class SongSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    artist_name = serializers.CharField(source='artist.name', read_only=True)
    
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist_name', 'genre','genre_name', 'release_year']               