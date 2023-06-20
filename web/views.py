from typing import Any
from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reviews, Places
from .forms import ReviewForm, PlaceForm, PhotoForm


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


class NewReview(LoginRequiredMixin, generic.CreateView):
    placeForm = PlaceForm
    reviewForm = ReviewForm
    photosForm = PhotoForm
    login_url = "/loggain"
    template_name = "new-review.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
             'placesForm': self.placeForm, 
             'reviewsForm': self.reviewForm,
             'photosForm': self.photosForm
             })
    

    def post(self, request, *args, **kwargs):
            placeform = self.placeForm(request.POST)
            reviewForm = self.reviewForm(request.POST)
            photoForm = self.photosForm(request.POST, request.FILES)
            
            if placeform.is_valid() and reviewForm.is_valid() and photoForm.is_valid():
                reviewForm.instance.author = self.request.user
                placeform.instance.created_by = self.request.user
                
                place = placeform.save(commit=False)
                review = reviewForm.save(commit=False)

                review.place = place

                place.save()
                review.save()

                if len(photoForm.data) > 0:
                    photo = photoForm.save(commit=False)
                    photo.review = review
                    photo.save()

                return redirect('places-detail', pk=place.id)

            return render(request, self.template_name, {
                 'placesForm': placeform,
                 'reviewsForm': reviewForm,
                 'photosForm': photoForm,
                 }, status=400)


class PlacesDeleteView(LoginRequiredMixin, generic.DeleteView):
     model = Places
     login_url = "/loggain"
     success_url = "/platser"

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