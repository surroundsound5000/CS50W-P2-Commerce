from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import *
from .forms import ListingForm 


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': listings
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = Listing(
                seller = request.user, 
                active = True, 
                **form.cleaned_data)
            new_listing.save()

            #Create a 'bid' matching the starting price. 
            
            create_bid(new_listing, request.user, new_listing.starting_bid)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/newlisting.html", {
                "form": form
                })
    else:
        form = ListingForm()
        return render(request, "auctions/newlisting.html", {
            "form": form
            })
    
def create_bid(bid_listing, bid_user, bid_amount):
    ''' Takes an amount (max_digits=8, decimal_places=2) and a user and listing model, then saves them as a new Bid entry'''
    new_bid = Bid(
        amount = bid_amount,
        user = bid_user,
        listing = bid_listing
    )
    new_bid.save()
