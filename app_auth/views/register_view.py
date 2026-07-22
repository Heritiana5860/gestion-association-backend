from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        full_name = request.data.get('fullName')
        username = request.data.get('username')
        password = request.data.get('password')

        # Vérifier si le username existe déjà
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Créer l’utilisateur
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=full_name  
        )

        # Générer JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "fullName": user.first_name
        }, status=status.HTTP_201_CREATED)