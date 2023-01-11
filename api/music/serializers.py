from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        models = Songs
        fields = ("title", "artist")