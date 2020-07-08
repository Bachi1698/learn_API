from rest_framework import viewsets
from . import serializers
from . import models

class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

class CarousolViewSet(viewsets.ModelViewSet):
    queryset = models.Carousol.objects.all()
    serializer_class = serializers.CarousolSerializer

class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = models.SiteInfo.objects.all()
    serializer_class = serializers.SiteInfoSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer