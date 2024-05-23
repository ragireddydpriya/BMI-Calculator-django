from django.urls import path,include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bmi', views.BMIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]