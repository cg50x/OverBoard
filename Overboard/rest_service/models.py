from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=45)
    created_on = models.DateField()
    
    def __unicode__(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=45)
    board = models.ForeignKey(Board)
    position = models.IntegerField()
    
    def __unicode__(self):
        return self.board.name + " - " + self.name

class Card(models.Model):
    title = models.CharField(max_length=45)
    created_on = models.DateField()
    creator = models.ForeignKey(User)
    column = models.ForeignKey(Column)
    
    def __unicode__(self):
        return self.title

class BoardPermission(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    can_read = models.BooleanField()
    can_write = models.BooleanField()
    
    def __unicode__(self):
        return self.user.username + " - " + self.board.name