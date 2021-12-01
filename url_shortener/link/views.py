from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Link
from .forms import URLPostForm
from .shorten import short

# Create your views here.

def index(req):
    #return HttpResponse("<h1>Welcome to URL Shortener<h1>")
    return render(req, 'index.html')

def show(req, link):
    site = Link.objects.get(url=link)
    return HttpResponse(f'<h3>URL: {site.website}!</h3>')

def realurl(req, token):
    url = Link.objects.filter(shortUrl=token)[0] 
    return redirect(url.url) 

def submitUrl(req):
    if req.method == 'POST':
        form = URLPostForm(req.POST)
        token = " "
        if form.is_valid():
            newUrl = form.save(commit=False)
            token = short().issue_token()
            newUrl.shortUrl = token
            newUrl.save()
            url = form.cleaned_data.get('url')
            print(url)
    else:
        form = URLPostForm()
        token = "Invalid Token"
        data = {'form': form, 'token':token}
        print(data)
        return render(req, 'create.html', data)


