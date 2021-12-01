from django import forms
from .models import Link
import random

class URLPostForm(forms.Form):
    """ url = forms.CharField(max_length=200)
    shortUrl = forms.CharField(max_length=6) """
    
    class Meta:
        model = Link
        fields = ['url']