from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer

# Create your views here.
class ListSongView(generics.ListAPIView):
    #Provides a get method handler.
    queryset = Songs.objects.all()
    serializer_class = SongSerializer