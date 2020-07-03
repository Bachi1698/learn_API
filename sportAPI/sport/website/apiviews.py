from rest_framework import viewsets
from . import serializers
from . import models

class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = models.SiteInfo.objects.all()
    serializer_class = serializers.SiteInfoSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = models.Newsletter.objects.all()
    serializer_class = serializers.NewsletterSerializer

class CarousolViewSet(viewsets.ModelViewSet):
    queryset = models.Carousol.objects.all()
    serializer_class = serializers.CarousolSerializer

class ReseauViewSet(viewsets.ModelViewSet):
    queryset = models.Reseau.objects.all()
    serializer_class = serializers.ReseauSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer