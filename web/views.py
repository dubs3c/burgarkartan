from typing import Any
from django.shortcuts import render
from django.views import generic
from django.db.models import Count

from .models import Reviews, Places


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


class PlacesView(generic.ListView):
    queryset = Reviews.objects.values("place__id", "place__name", "place__rating", "place__location").annotate(reviews=Count("id"))
    template_name = "places.html"
    context_object_name = "places"


class PlacesDetailView(generic.DetailView):
    model = Places
    template_name = "places-detail.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["reviews"] = Reviews.objects.filter(place=self.kwargs['pk'])
            return context