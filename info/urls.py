from django.urls import path, include
from info.views import MemberViewSet, EventViewSet, CotisationViewSet, AdhasionAnnuelViewSet, CadreViewSet, PresidentViewSet, HonneurViewSet, CollegeViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'event', EventViewSet)
router.register(r'cotisation', CotisationViewSet)
router.register(r'annuel', AdhasionAnnuelViewSet)
router.register(r'cadre', CadreViewSet)
router.register(r'president', PresidentViewSet)
router.register(r'honneur', HonneurViewSet)
router.register(r'college', CollegeViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
