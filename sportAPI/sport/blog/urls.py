from django.urls import path
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('commentaire', apiviews.CommentaireViewSet, basename='commentaire')
router.register('article', apiviews.ArticleViewSet, basename='article')
router.register('tag', apiviews.TagViewSet, basename='tag')
router.register('categorie', apiviews.CategorieViewSet, basename='categorie')



urlpatterns = [

    ]

urlpatterns += router.urls