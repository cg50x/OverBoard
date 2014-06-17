from rest_service.models import (
    Board, 
    Column, 
    Card, 
    BoardPermission
)
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'created_on')

class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Column
        fields = ('name', 'board', 'position')
        
class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('title', 'created_on', 'creator', 'column')
        
class BoardPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardPermission
        fields = ('user','board', 'can_read', 'can_write')