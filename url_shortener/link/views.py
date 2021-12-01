from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Link
from .forms import URLPostForm

# Create your views here.

def index(req):
    #return HttpResponse("<h1>Welcome to URL Shortener<h1>")
    form = URLPostForm()
    data = {'form':form}
    return render(req, 'home.html', data)

def show(req, link):
    site = Link.objects.get(url=link)
    return HttpResponse(f'<h3>URL: {site.website}!</h3>')

