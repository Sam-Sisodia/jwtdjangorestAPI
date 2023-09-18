from django.shortcuts import render
from  . serializer import *
from rest_framework import generics
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView ,InvalidToken
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout


# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    queryset = ""
    permission_classes = ()
    serializer_class = RegisterSerializer


# class LoginAPIView(TokenObtainPairView):
#     serializer_class = LoginSerializer
#     permission_classes = ()


class GetJwtToken(APIView):
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request=request, email=email, password=password)
        if user:
            serializer = LoginSerializer(
                data=request.data, context={"request": request}
            )
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                raise InvalidToken(e.args[0])
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        
        return Response(
            {"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class Studentdetail(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
