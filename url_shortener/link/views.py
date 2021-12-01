from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Link
from .forms import URLPostForm
from .shorten import short
import webbrowser
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(req):
    return render(req, 'index.html')

def show(req, link):
    site = Link.objects.get(url=link)
    return HttpResponse(f'<h3>URL: {site.website}!</h3>')

def realurl(req, token):
    url = Link.objects.filter(shortUrl=token)[0] 
    return redirect(url.url) 

def submitUrl(req):
    data = {'form': '', 'token':''}
    if req.method == 'POST':
        form = URLPostForm(req.POST)
        token = " "
        if form.is_valid():
            newUrl = form.save(commit=False)        
            token = short().issue_token()
            newUrl.shortUrl = token
            newUrl.save()
            print(newUrl.url)
            print(newUrl.shortUrl)         
            return HttpResponse(f'<a href="http://127.0.0.1:8000/{newUrl.shortUrl}"> http://127.0.0.1:8000/{newUrl.shortUrl} </a>')
    else:
        form = URLPostForm()
        token = "Invalid Token"
        data = {'form': form, 'token':token}
    return render(req, 'create.html', data)


def findWebsite(self, address):

    try:
        website = Link.objects.get(shortUrl=address)
    except ObjectDoesNotExist:
        return redirect('submitURL')

    webbrowser.open(website.url)
    return HttpResponse(f'{website.url}')


