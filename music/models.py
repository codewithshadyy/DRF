from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"This is {self.name}"

      
class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="artists")
    
    def __str__(self):
        return f"This is {self.name}"
    
     
    
class  Song(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="songs")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")  
    release_year = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.artist}"    
