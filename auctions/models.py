from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass 

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.CharField(max_length=64, blank=True, null=True)
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2, default = 0, blank=True)
    active = models.BooleanField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="winner")

    def __str__(self):
        return f"{self.id}: {self.title} ({self.description})"

class Bid(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

