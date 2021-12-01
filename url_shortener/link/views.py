from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("<h1>Welcome to URL Shortener<h1>")

def show(req, url):
    return HttpResponse(f'<h3>URL: {url}!</h3>')