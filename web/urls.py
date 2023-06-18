from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("om", views.about, name="about"),
    path("platser", views.PlacesView.as_view(), name="places"),
    path("platser/<int:pk>", views.PlacesDetailView.as_view(), name="places-detail"),
]