from django.forms import ModelForm, ImageField
from .models import Reviews, Photos, Places


class PlaceForm(ModelForm):
    prefix = "places"
    class Meta:
        model = Places
        fields = ["name", "location"]


class ReviewForm(ModelForm):
    prefix = "reviews"
    class Meta:
        model = Reviews
        fields = ["review", "rating"]
        


class PhotoForm(ModelForm):
    prefix = "photos"
    photo = ImageField(required=False)
    class Meta:
        model = Photos
        fields = ["photo"]