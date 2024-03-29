"""
URL configuration for RiffMates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# RiffMates/RiffMates/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from ninja import NinjaAPI
from home.api import router as home_router
from promoters.api import router as promoters_router
from bands.api import router as venues_router
from bands.views import get_venues

api = NinjaAPI(version="1.0.0")
api.add_router("/home/", home_router)
api.add_router("/promoters/", promoters_router)
api.add_router("/bands/", venues_router)

urlpatterns = [
    path('', home_views.home, name="home"),
    path('tables/', home_views.tables, name="tables"),
    path('bands/',include("bands.urls")),
    path('content/',include("content.urls")),
    path('promoters/', include("promoters.urls")),
    path('admin/', admin.site.urls),
    path('credits/', home_views.view_credits, name="credits"),
    path('about/', home_views.view_about, name='about'),
    path('news/', home_views.view_news, name="news"),
    path('venues/', get_venues, name="venues"),
    path('accounts/', include('django.contrib.auth.urls')),
    # Home API
    path("api/v1/", api.urls), # Add the API endpoints as URLs
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
# static() function takes two arguments: the base URL to serve from, and the location of the files; it returns a URL configuration that can be used to serve files in DEBUG mode
