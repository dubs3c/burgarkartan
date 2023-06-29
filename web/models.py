from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.


class Places(models.Model):
    name = models.TextField()
    website = models.TextField(blank=True)
    location = models.TextField()
    rating = models.FloatField(default=0.0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "places"
        verbose_name = "place"

    def __str__(self):
        return f"{self.name}(rating={self.rating})"


class Reviews(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "reviews"
        verbose_name = "review"

    def __str__(self):
        return f"{self.author.username}(place={self.place.name}, rating={self.rating})"

    def save(self, *args, **kwargs):
        # TODO: has to be a race condition here
        # investigate if the following code can be wrapped inside a transaction
        super().save(*args, **kwargs)
        average_rating = Reviews.objects.filter(place__name=self.place.name).aggregate(
            Avg("rating")
        )
        self.place.rating = average_rating.get("rating__avg")
        self.place.save()


class Photos(models.Model):
    photo = models.ImageField()
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "photos"
        verbose_name = "photo"


class Teams(models.Model):
    name = models.TextField()
    description = models.TextField()
    admin = models.ForeignKey(User, related_name="team_admin", on_delete=models.PROTECT)
    users = models.ManyToManyField(User)
    favourites = models.ManyToManyField(Places)

    class Meta:
        verbose_name_plural = "teams"
        verbose_name = "team"

    def __str__(self):
        return self.name
