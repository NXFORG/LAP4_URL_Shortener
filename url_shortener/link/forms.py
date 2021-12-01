from django import forms
from .models import Link

class URLPostForm():
    url = forms.CharField(max_length=200)
    website = forms.CharField(max_length=20)

    class Meta:
        model = Link
        fields = ['url', 'website']