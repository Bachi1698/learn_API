from rest_framework import serializers
from . import models

class ClassementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classement
        fields = '__all__'

class EntrainementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entrainement
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'
    
class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Joueur
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Match
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = '__all__'