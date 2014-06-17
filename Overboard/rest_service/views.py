from django.contrib.auth.models import User
from rest_service.models import (
    Board,
    Column,
    Card,
    BoardPermission
)
from rest_framework import viewsets
from rest_service.serializers import (
    UserSerializer,
    BoardSerializer,
    ColumnSerializer,
    CardSerializer,
    BoardPermissionSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class BoardPermissionViewSet(viewsets.ModelViewSet):
    queryset = BoardPermission.objects.all()
    serializer_class = BoardPermissionSerializer

