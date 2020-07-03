from rest_framework import serializers
from . import models
 
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newsletter
        fields = '__all__'

class CarousolSerializer(serializers.ModelSerializer):
    carousol_site = SiteInfoSerializer(many=True, required=False)
    class Meta:
        model = models.Carousol
        fields = '__all__'

class ReseauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reseau
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    staff_about = AboutSerializer(many=True, required=False)
    class Meta:
        model = models.Staff
        fields = '__all__'