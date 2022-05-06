from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^series/$', views.serie_list),
    re_path(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),
]