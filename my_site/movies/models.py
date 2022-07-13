from django.db import models

# Create your models here.

class MoviesData( models.Model ):
    def __str__(self):
        return self.name

    name = models.CharField( max_length= 200 )
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField( max_length= 200, default= 'action' )