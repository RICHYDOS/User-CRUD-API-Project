from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers', CustomerViewSet, basename="customers")

urlpatterns = router.urls
