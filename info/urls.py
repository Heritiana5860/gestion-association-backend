from django.urls import path, include
from info.views import MemberViewSet, EventViewSet, CotisationViewSet, AdhasionAnnuelViewSet, CadreViewSet, PresidentViewSet, HonneurViewSet, CollegeViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'event', EventViewSet, basename='event')
router.register(r'cotisation', CotisationViewSet, basename='cotisation')
router.register(r'annuel', AdhasionAnnuelViewSet)
router.register(r'cadre', CadreViewSet)
router.register(r'president', PresidentViewSet)
router.register(r'honneur', HonneurViewSet)
router.register(r'college', CollegeViewSets, basename='college')

urlpatterns = [
    path('', include(router.urls)),
]
