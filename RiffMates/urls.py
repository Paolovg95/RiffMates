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
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from bands.views import get_venues

urlpatterns = [
    path('bands/',include("bands.urls")),
    path('admin/', admin.site.urls),
    path('credits/', home_views.view_credits, name="credits"),
    path('about/', home_views.view_about, name='about'),
    path('news/', home_views.view_news, name="news"),
    path('venues/', get_venues, name="venues")

]
