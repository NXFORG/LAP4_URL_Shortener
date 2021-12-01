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
    print("realurl")
    url = Link.objects.filter(shortUrl=token)[0] 
    return redirect(url.url) 

def submitUrl(req):
    data = {'form': '', 'token':''}
    if req.method == 'POST':
        form = URLPostForm(req.POST)
        token = " "
        print("gets here")
        if form.is_valid():
            print("gets here")
            # url = form.cleaned_data.get('url')
            newUrl = form.save(commit=False)
            # username = form.cleaned_data.get('username')
            token = short().issue_token()
            # url.shortUrl= token
            # url.save()
            newUrl.shortUrl = token
            newUrl.save()
            
            print("if")
            print(newUrl)
            return HttpResponse(f'<h3> {newUrl}!</h3>')
            # return redirect('index')
    else:
        print("else")
        form = URLPostForm()
        token = "Invalid Token"
        data = {'form': form, 'token':token}
    return render(req, 'create.html', data)


