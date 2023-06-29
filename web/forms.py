from .models import Reviews, Photos, Places

from django.forms import ModelForm, ImageField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
