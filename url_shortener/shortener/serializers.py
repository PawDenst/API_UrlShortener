from rest_framework import serializers
from .models import ShortURL

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['long_url']
