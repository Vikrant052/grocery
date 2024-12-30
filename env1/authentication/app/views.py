from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import CustomUser
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class RegisterView(generics.CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = RegistrationSerializer
  
  
class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer
  
  def post(self, request, *args, **kwargs):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email,password=password)
    if user is not None:
      refresh = RefreshToken.for_user(user)
      user_serializer = CustomUserSerializer(user)
      return Response({
        'refresh': str(refresh), 
        'access': str(refresh.access_token),
        'user': user_serializer.data
        })
    else:
      return Response({'message':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
                       



