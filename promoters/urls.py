from django.urls import path
from promoters import views
urlpatterns = [
    path("promoters/", views.promoters),
    path("partial_promoters/", views.partial_promoters)
]
