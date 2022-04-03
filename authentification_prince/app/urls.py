from django.urls import path

from app.views import hello,register,loginView,logoutView

urlpatterns = [
    path("",hello,name="home"),
    path("register",register,name="register"),
    path("login",loginView,name="login"),
    path("logout",logoutView,name="logout")
]
