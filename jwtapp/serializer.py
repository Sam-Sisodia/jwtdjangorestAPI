
from django.contrib.auth import get_user_model
from . models import *

from rest_framework import serializers

from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer






class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["email","mobile","password"]



class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            token = super().get_token(user)

            token["email"] = user.email
            token["is_superuser"] = user.is_superuser     #send the extra fields of User inside the token 

            return token
        except Exception as e:
            raise ValidationError("Something went wrong")




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"