from django.contrib import admin
from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router.register("students",views.Studentdetail,basename="students")

router.register("register",views.RegisterView,basename="register")

urlpatterns = [
    # path(views.jj.as_view())

    path("login/",views.GetJwtToken.as_view())

    
   
]+router.urls
