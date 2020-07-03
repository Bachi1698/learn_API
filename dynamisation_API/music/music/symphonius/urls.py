from django.urls import path
from . import apiviews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tour', apiviews.TourViewSet, basename='tour')
router.register('video', apiviews.VideoViewSet, basename='video')
router.register('album', apiviews.AlbumViewSet, basename='album')
router.register('musique', apiviews.MusiqueViewSet, basename='musique')
router.register('equipe', apiviews.EquipeViewSet, basename='equipe')
router.register('equipe', apiviews.GallerieViewSet, basename='equipe')


urlpatterns = [

    ]

urlpatterns += router.urls