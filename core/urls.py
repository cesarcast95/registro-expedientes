from django.urls import path
#Aqui se importa las CBV que hciimos en las views.py
from .views import HomePageView, SamplePageView

urlpatterns = [
    #Aqui utilizamos nuestras CBV
    path('', HomePageView.as_view(), name="home"),
]