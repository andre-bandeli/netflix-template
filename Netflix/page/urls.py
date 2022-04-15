from django.urls import path
from .views import index, login, users

app_name = "page"

urlpatterns = [

    path("/", index, name="index"),
    path("login/", login, name="login"),
    path("usuarios/", users, name="usuarios"),
]