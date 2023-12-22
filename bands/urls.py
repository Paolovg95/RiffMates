from django.urls import path
from bands import views

urlpatterns = [
    path('musician/<int:musician_id>/', views.get_musician, name="musician"),
    path('musicians', views.get_musicians, name="musicians"),
    path('<str:band_name>', views.get_band, name="band")
]
