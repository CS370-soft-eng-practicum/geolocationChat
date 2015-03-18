from django.db import models


# Create your models here.

class Page(models.Model):
    createDate = models.DateTimeField('date created')
    topic = models.CharField(max_length = 60)
    createUser = models.User('created this user')
    location = models.ForeignKey(RegionCoordinates)

class Comment(models.Model):
    text = models.CharField(max_length= 200)
    postDate = models.DateTimeField('date published')
    poster = models.User('person posting')

class RegionCoordinates(models.Model):
    x1 = models.FloatField()
    y1 = models.FloatField()
    x2 = models.FloatField()
    y2 = models.FloatField()


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):




