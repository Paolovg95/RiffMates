from django.urls import path
from bands import views

urlpatterns = [
    path('', views.get_bands, name="bands"),
    path('musician/<int:musician_id>/', views.get_musician, name="musician"),
    path('musicians', views.get_musicians, name="musicians"),
    path('<str:band_id>', views.get_band, name="band"),
    path('restricted_musician/<int:musician_id>/', views.musician_restricted),
    path('restricted_venues/', views.venues_restricted)
]
