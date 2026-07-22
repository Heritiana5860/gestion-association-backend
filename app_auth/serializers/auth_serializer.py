from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Ajouter des champs personnalisés
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['role'] = self.user.role
        
        return data
