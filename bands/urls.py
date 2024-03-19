from django.urls import path
from bands import views

urlpatterns = [
    path('', views.get_bands, name="bands"),
    path('musician/<slug:slug>/', views.get_musician, name="musician"),
    path('musicians', views.get_musicians, name="musicians"),
    path('venues', views.get_venues, name="venues"),
    path('<str:band_id>', views.get_band, name="band"),
    path('my_musicians/', views.musicians_restricted, name='musician_profiles_restricted'),
    path('my_venues/', views.venues_restricted, name="my_venues_restricted"),
    path('my_venues/edit/<int:venue_id>/', views.edit_venues, name="edit_venue"),
    path('my_profiles/edit/<int:musician_id>/', views.edit_musician, name="edit_musician"),
    path('my_profiles/new/', views.edit_musician, name="new_musician"),
    path('my_venues/new/', views.edit_venues, name="new_venue"),
    path('search_musicians/', views.search_musicians, name="search_musicians")
]
