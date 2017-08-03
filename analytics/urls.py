from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.overview, name = "overview"),
    url(r'^details/(?P<nip_pk>\d+)/$', views.nip_details, name = "details"),
    url(r'^login/$', views.login_user, name = "login"),
    url(r'^logout/$', views.logout_user, name = "logout"),
    url(r'^get_historical_data/(?P<nip_pk>\d+)/(?P<timescale>[\w\-]+)/$', views.get_historical_data, name = "getHistoricalData"),
]