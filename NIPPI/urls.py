"""NIPPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^analytics/', include('analytics.urls', namespace = "analytics")),
    url(r'^management/', include('management.urls', namespace = "management")),
    url(r'^nips/', include('nips.urls', namespace = "nips")),
    url(r'^receiver/', include('receiver.urls', namespace = "receiver")),
    url(r'^analytrecordsics/', include('records.urls', namespace = "records")),
    url(r'^siren/', include('siren.urls', namespace = "siren")),
]
