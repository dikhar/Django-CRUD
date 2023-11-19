from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from api.views import CompanyViewSet,HumidityViewSet,TempViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('device' , CompanyViewSet)
router.register('humidity', HumidityViewSet)
router.register('temperature', TempViewSet)
#router.register('devices-graph', DeviceGraphViewSet, basename='devices-graph')
#router.register('devices/{device uid}/readings', ReadingViewset, basename='readings')
urlpatterns = [
    path('', include(router.urls))
]
