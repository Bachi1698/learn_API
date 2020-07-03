from rest_framework import viewsets
from . import serializers
from . import models

class TourViewSet(viewsets.ModelViewSet):
    queryset = models.Tour.objects.all()
    serializer_class = serializers.TourSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class MusiqueViewSet(viewsets.ModelViewSet):
    queryset = models.Musique.objects.all()
    serializer_class = serializers.MusiqueSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = models.Equipe.objects.all()
    serializer_class = serializers.EquipeSerializer

class GallerieViewSet(viewsets.ModelViewSet):
    queryset = models.Gallerie.objects.all()
    serializer_class = serializers.GallerieSerializer