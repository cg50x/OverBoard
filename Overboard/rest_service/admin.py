from django.contrib import admin
from rest_service.models import User, Board, Column, Card, BoardPermission

# Register your models here.
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Card)
admin.site.register(BoardPermission)