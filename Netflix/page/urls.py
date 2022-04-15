from django.urls import path
from .views import index, login, users, index_user_2, index_user_3

app_name = "page"

urlpatterns = [

    path("", index, name="index"),
    path("user2/", index_user_2, name="index_user_2"),
    path("user3/", index_user_3, name="index_user_3"),
    path("login/", login, name="login"),
    path("usuarios/", users, name="usuarios"),
]