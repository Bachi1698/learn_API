from django.urls import path
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('video', apiviews.VideoViewSet, basename='video')
router.register('match', apiviews.MatchViewSet, basename='match')
router.register('joueur', apiviews.JoueurViewSet, basename='joueur')
router.register('sponsor', apiviews.SponsorViewSet, basename='sponsor')
router.register('entrainement', apiviews.EntrainementViewSet, basename='entrainement')
router.register('classement', apiviews.ClassementViewSet, basename='classement')



urlpatterns = [

    ]

urlpatterns += router.urls