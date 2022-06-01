import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import Http404
from .models import ImagePost, ImageCategory, ImageLocation




# Create your views here.

def landing(request):
    posts = ImagePost.objects.all()
    post_list = []
    for post in posts:
        if post.recently_uploaded():
            post_list.append(post)
            return render(request,'album/landing.html',{"post_list":post_list})
        else:
         return render(request, 'album/index.html')


def index(request):
    posts = ImagePost.objects.all()

    context = {
        "posts":posts
    }
    return render(request, 'album/index.html',context)


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imageposts = ImagePost.search_image(search_term)

        message = f"{search_term}"



        context = {
            "message":message,
            "posts":searched_imageposts
        }

        return render(request, 'album/search.html', context)


    else:
        message = "You haven't searched for any term"

        return render(request,'album/search.html',{"message":message})


def nature_images(request):
    images=ImagePost.objects.filter(image_category__name="nature")

    context = {
        "posts":images
    }
    return render(request, 'album/display.html', context)



def park_images(request):
    images=ImagePost.objects.filter(image_category__name="park")

    context = {
        "posts":images
    }
    return render(request, 'album/display.html', context)

def beach_images(request):
    images=ImagePost.objects.filter(image_category__name="beach")

    context = {
        "posts":images
    }
    return render(request, 'album/display.html', context)

def cgi_images(request):
    images=ImagePost.objects.filter(image_category__name="cgi")

    context = {
        "posts":images
    }
    return render(request, 'album/display.html', context)


def unknown_images(request):
    images=ImagePost.objects.filter(image_category__name="Unknown")

    context = {
        "posts":images
    }
    return render(request, 'album/display.html', context)