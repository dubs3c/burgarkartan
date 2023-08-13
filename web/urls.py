from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("om", views.about, name="about"),
    path(
        "loggain",
        auth_views.LoginView.as_view(
            template_name="loggain.html",
            next_page="/",
            redirect_authenticated_user=True,
        ),
        name="loggain",
    ),
    path("loggaut", auth_views.LogoutView.as_view(next_page="/"), name="loggaut"),
    path("nyrecension", views.NewReview.as_view(), name="new-review"),
    path("platser", views.PlacesView.as_view(), name="places"),
    path("platser/<slug:slug>", views.PlacesDetailView.as_view(), name="places-detail"),
    path(
        "platser/<int:pk>/delete",
        views.PlacesDeleteView.as_view(),
        name="places-delete",
    ),
    path("platser/<int:pk>/nyrecension",
         views.PlacesAddReview.as_view(),
         name="places-review-add"),
    path("profile", views.ProfileView.as_view(), name="profile"),
]
