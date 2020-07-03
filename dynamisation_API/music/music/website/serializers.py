from rest_framework import serializers
from . import models

class AboutSerializer(serializer.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'

class SiteInfoSerializer(serializer.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields ='__all__'

class CarousolSerializer(serializer.ModelSerializer):
    class Meta:
        model = models.Carousol
        fields = '__all__'

