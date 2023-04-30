from django.urls import path

from . import views

app_name = "call"

urlpatterns = [
    path("signup", view=views.RegisterUser.as_view(), name="signup"),
    path("login", view=views.LoginUser.as_view(), name="login"),
]
