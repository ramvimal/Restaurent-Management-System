from django.urls import path , include
from . import views 
urlpatterns = [
    path("login_user/", views.login_view, name="login_user"),
    path("Register_user/", views.register_view, name="register_user"),
    path("logout_user/", views.logout_view, name="logout_user"),
]

