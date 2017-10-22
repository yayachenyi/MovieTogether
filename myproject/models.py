from django.db import models

class Movie(models.Model):
	movieId = models.movieId(max_length=8, unique=True)
	title = models.title(max_length=100)
	genres = models.genres(max_length=100)

	def __unicode__(self):
		return self.movieId
