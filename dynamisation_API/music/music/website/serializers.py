from rest_framework import serializers
from . import models

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields ='__all__'

class CarousolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carousol
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'
