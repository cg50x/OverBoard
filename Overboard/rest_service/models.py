from django.db import models

# Create your models here.
class User(models.Model):
    username      = models.CharField(max_length=45)
    password_hash = models.CharField(max_length=100)
    salt          = models.CharField(max_length=100)
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    email         = models.EmailField()
    
    def __unicode__(self):
        return self.username

class Board(models.Model):
    name = models.CharField(max_length=45)
    created_on = models.DateField()
    
    def __unicode__(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=45)
    board = models.ForeignKey(Board)
    position = models.IntegerField()

class Card(models.Model):
    title = models.CharField(max_length=45)
    created_on = models.DateField()
    creator = models.ForeignKey(User)
    column = models.ForeignKey(Column)

class BoardPermission(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    can_read = models.BooleanField()
    can_write = models.BooleanField()