from rest_framework import viewsets
from . import serializers
from . import models

class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = models.Match.objects.all()
    serializer_class = serializers.MatchSerializer

class JoueurViewSet(viewsets.ModelViewSet):
    queryset = models.Joueur.objects.all()
    serializer_class = serializers.JoueurSerializer

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer

class EntrainementViewSet(viewsets.ModelViewSet):
    queryset = models.Entrainement.objects.all()
    serializer_class = serializers.EntrainementSerializer

class ClassementViewSet(viewsets.ModelViewSet):
    queryset = models.Classement.objects.all()
    serializer_class = serializers.ClassementSerializer