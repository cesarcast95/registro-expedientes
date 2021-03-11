from django.urls import path, include
from .views import RegistroListView, RegistroCreated, RegistroUpdate, RegistroDetailView, search#, PagesDetailView
# from .views import PageCreate, PageUpdate, PageDelete
from . import views


registry_patterns = ([
    path('', RegistroListView.as_view(), name='registry'),
    path('<int:pk>/<slug:slug>/', RegistroDetailView.as_view(), name='registro'),
    path('create/', RegistroCreated.as_view(), name='create'),
    path('update/<int:pk>/', RegistroUpdate.as_view(), name='update'),
    path('search/', views.search, name="search"),
], 'registry')