from .models import Reviews, Photos, Places

from django import forms
from django.forms import ModelForm, ImageField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class PlaceForm(ModelForm):
    prefix = "places"

    class Meta:
        model = Places
        fields = ["name", "location"]

    def clean_location(self):
        slug = slugify(self.cleaned_data["location"])
        if Places.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Det här burgarhaket finns redan")
        return slug


class ReviewForm(ModelForm):
    prefix = "reviews"

    class Meta:
        model = Reviews
        fields = ["review", "rating"]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating >= 1 and rating <= 5:
            return rating
        else:
            raise forms.ValidationError("Välj 1-5")


class PhotoForm(ModelForm):
    prefix = "photos"
    photo = ImageField(required=False)

    class Meta:
        model = Photos
        fields = ["photo"]


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        exclude = ("email",)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if email:
            found = User.objects.get(email=email)

            if found:
                raise ValidationError("Tyvärr kan du inte byta till den email adressen")
