from rest_framework import viewsets
from . import serializers
from . import models

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = models.Commentaire.objects.all()
    serializer_class = serializers.CommentaireSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer