from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path('search', views.search, name="search"),
    path("wiki/<str:entry>", views.entries, name="entries")
]
