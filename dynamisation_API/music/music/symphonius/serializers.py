from rest_framework import serializers
from . import models

class GallerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallerie
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipe
        fields = '__all__'

class MusiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Musique
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    album_musque = MusiqueSerializer(many=True, required=False)
    class Meta:
        model = models.Album
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour
        fields = '__all__'