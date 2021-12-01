from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.submitUrl, name='submitURL'),
    path('create/<str:link>', views.submitUrl, name='submitURL'),
    path('<str:address>', views.findWebsite, name='findWebsite')

]