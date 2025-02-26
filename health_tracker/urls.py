"""
URL configuration for health_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fitness/', include('fitness.urls')),
    re_path(r'^$', RedirectView.as_view(url='/fitness/', permanent=True)),
]


# Custom error handlers (MUST be outside urlpatterns)
from django.conf.urls import handler404
from fitness.views import custom_404

handler404 = custom_404  # Assign the custom 404 handler
