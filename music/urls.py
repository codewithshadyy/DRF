
from django.urls import path

from .views import CreateArtistAPIView, CreateGenreAPIView, CreateSongAPIView, ListArtistAPIView, ListGenreAPIView, ListSongAPIView

urlpatterns = [
    path('songs/', ListSongAPIView.as_view(), name='songs'),
    path('songs/create/', CreateSongAPIView.as_view(), name='create-song'),
    path('artists/', ListArtistAPIView.as_view(), name='artists'),
    path('artist/create/', CreateArtistAPIView.as_view(), name='create-artist'),
    path('genres/', ListGenreAPIView.as_view(), name='genre'),
    path('genres/create/', CreateGenreAPIView.as_view(), name='genre-artist')
    
]
