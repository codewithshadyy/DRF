from django.shortcuts import render

from .serializers import SongSerializer, ArtistSerializer, GenreSerializer
from .models import Song, Artist, Genre
from rest_framework.generics import(
    ListAPIView,
    CreateAPIView
)
from rest_framework.permissions import(
    IsAuthenticated, 
    IsAdminUser,
    AllowAny
)

class ListGenreAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
    
class CreateGenreAPIView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]
    
    
class ListArtistAPIView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
    
    
class CreateArtistAPIView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]
        
        
    
    

class  ListSongAPIView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [AllowAny]
    
class CreateSongAPIView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminUser]  
    
