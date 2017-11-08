from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genres  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.movieId
