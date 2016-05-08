from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.
class Genre(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    context = models.CharField(max_length=200, null = True, blank= True)

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ["-name"]

    def __unicode__(self):
        return self.name

class Track(models.Model):
    genre = models.ForeignKey('Genre', null = True)
    name = models.CharField(max_length=30, unique= True)
    ratings = GenericRelation(Rating, related_query_name='Tracks')
    # ratings = GenericRelation(Rating, related_query_name='Tracks')
    
    class Meta:
        verbose_name_plural = "Tracks"
        ordering = ["-name"]
        
    # def get_absolute_url(self):
    #       return reverse('tracks')
    
    def __unicode__(self):
        return self.name


