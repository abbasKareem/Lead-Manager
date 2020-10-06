from django.urls import path, include

from rest_framework.routers import DefaultRouter
from leads import api

router = DefaultRouter()
router.register('api/leads', api.LeadViewSets, basename='leads')

urlpatterns = router.urls
