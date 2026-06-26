from .member_view import MemberViewSet
from .event_view import EventViewSet
from .cotisation_view import CotisationViewSet
from .annuel_view import AdhasionAnnuelViewSet
from .cadre_view import CadreViewSet
from .president_view import PresidentViewSet
from .honneur_view import HonneurViewSet
from .college_view import CollegeViewSets

__all__ = [
    'MemberViewSet', 
    'EventViewSet', 
    'CotisationViewSet', 
    'AdhasionAnnuelViewSet', 
    'CadreViewSet', 
    'PresidentViewSet',
    'HonneurViewSet',
    'CollegeViewSets'
    ]