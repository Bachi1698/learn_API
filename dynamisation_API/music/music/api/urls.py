from django.urls import path
from symphonius import apiviews
from website import apiviews as websiteap
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tour', apiviews.TourViewSet, basename='tour')
router.register('video', apiviews.VideoViewSet, basename='video')
router.register('album', apiviews.AlbumViewSet, basename='album')
router.register('musique', apiviews.MusiqueViewSet, basename='musique')
router.register('equipe', apiviews.EquipeViewSet, basename='equipe')
router.register('equipe', apiviews.GallerieViewSet, basename='equipe')

router.register('contact', websiteap.ContactViewSet, basename='contact')

router.register('about', websiteap.AboutViewSet, basename='about')
router.register('carousol', websiteap.CarousolViewSet, basename='carousol')
router.register('site', websiteap.SiteInfoViewSet, basename='site')

urlpatterns = [

    ]

urlpatterns += router.urls