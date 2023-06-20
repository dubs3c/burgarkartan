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
                
                place = placeform.save(commit=False)
                review = reviewForm.save(commit=False)
                photo = photoForm.save(commit=False)

                review.place = place
                photo.review = review
                
                place.save()
                review.save()
                photo.save()
                
                return redirect('places-detail', pk=place.id)
            

            # If the forms are not valid render the page with the existing data
            return render(request, self.template_name, {
                 'placesForm': placeform,
                 'reviewsForm': reviewForm,
                 'photosForm': photoForm,
                 })


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