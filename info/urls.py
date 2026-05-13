from django.urls import path, include
from info.views import MemberViewSet, EventViewSet, CotisationViewSet, AdhasionAnnuelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'event', EventViewSet)
router.register(r'cotisation', CotisationViewSet)
router.register(r'annuel', AdhasionAnnuelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
