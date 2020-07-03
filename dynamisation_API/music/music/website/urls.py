from django.urls import path
from.import views 
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('about', apiviews.AboutViewSet, basename='about')
router.register('carousol', apiviews.CarousolViewSet, basename='carousol')
router.register('site', apiviews.SiteInfoViewSet, basename='site')

urlpatterns = [
        path('index',views.index,name='index'),
    ]

urlpatterns += router.urls