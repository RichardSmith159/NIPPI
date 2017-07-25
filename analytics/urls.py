from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.overview, name = "overview"),
    url(r'^details/(?P<nip_pk>\d+)/$', views.nip_details, name = "details"),
    url(r'^login/$', views.login_user, name = "login"),
]