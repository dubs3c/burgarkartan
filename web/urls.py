from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("om", views.about, name="about"),
    path("loggain", auth_views.LoginView.as_view(
        template_name = "loggain.html",
        next_page = "/",
        redirect_authenticated_user = True
        ), 
        name="loggain"),
    path("loggaut", auth_views.LogoutView.as_view(
        next_page = "/"
    ), name="loggaut"),
    path("platser", views.PlacesView.as_view(), name="places"),
    path("platser/<int:pk>", views.PlacesDetailView.as_view(), name="places-detail"),
]