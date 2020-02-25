"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from project import settings
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/',include('registration.backends.defaults.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('app1/',include('app1.urls')),
    path('',RedirectView.as_view(url="app1/")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
