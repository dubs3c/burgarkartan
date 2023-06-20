from django.forms import ModelForm
from .models import Reviews, Photos, Places


class PlaceForm(ModelForm):
    prefix = "places"
    class Meta:
        model = Places
        fields = ["name", "website", "location"]


class ReviewForm(ModelForm):
    prefix = "reviews"
    class Meta:
        model = Reviews
        fields = ["review", "rating"]
        


class PhotoForm(ModelForm):
    prefix = "photos"
    class Meta:
        model = Photos
        fields = ["photo"]