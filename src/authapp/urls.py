from django.urls import path

from authapp import views
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("register/", views.RegisterPageView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("update/<pk>", views.UserUpdateView.as_view(), name="update"),
]
