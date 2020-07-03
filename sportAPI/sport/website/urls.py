from django.urls import path
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('about', apiviews.AboutViewSet, basename='about')
router.register('contact', apiviews.ContactViewSet, basename='contact')
router.register('site', apiviews.SiteInfoViewSet, basename='site')
router.register('newsletter', apiviews.NewsletterViewSet, basename='newsletter')
router.register('entrainement', apiviews.CarousolViewSet, basename='entrainement')
router.register('reseau', apiviews.ReseauViewSet, basename='reseau')
router.register('staff', apiviews.StaffViewSet, basename='staff')



urlpatterns = [

    ]

urlpatterns += router.urls