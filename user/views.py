from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, EmailPasswordSerializer
# Create your views here.

from django.contrib.auth import authenticate

# View to register a user
class CreateUserView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View to get the token  
class TokenObtainView(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        serializer= EmailPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=email, password=password)
        
            if user:
                return Response({ "token": user.auth_token.key }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)