from rest_framework_simplejwt.views import TokenObtainPairView
from app_auth.serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
