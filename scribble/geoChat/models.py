from django.db import models
from django.contrib.auth.forms import User


# Create your models here.

class RegionCoordinates(models.Model):
    x1 = models.FloatField()
    y1 = models.FloatField()
    x2 = models.FloatField()
    y2 = models.FloatField()

class Page(models.Model):
    createDate = models.DateTimeField('date created')
    topic = models.CharField(max_length = 60)
    createUser = models.ForeignKey(User, blank=True, null=True)
    #createUser = models.User('created this user')
    location = models.ForeignKey(RegionCoordinates)

class Comment(models.Model):
    text = models.CharField(max_length= 200)
    postDate = models.DateTimeField('date published')
    name = models.CharField(max_length=12)

    def __unicode__ (self):
        return self.text
    #poster = models.ForeignKey(User, blank=True, null=True)

#chat room


class ChatRoom(models.Model):

    name = models.CharField(max_length=50)
    clients = []
    messages = []

    def __unicode__(self):
        return self.name

    def get_messages(self):
        return self.messages

    def add_client(self, client):
        self.clients.append(client)

    def add_message(self, message):
        self.messages.append(message)

    def remove_client(self, client):
        self.clients.remove(client)
