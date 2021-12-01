from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<str:link>', views.show, name='show'),
    path('create/', views.submitUrl, name='submitURL'),
    path('create/<str:link>', views.submitUrl, name='submitURL')

]