from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listings, name='listings'),
	url(r'^(?P<department>\w+)/$', views.listings, name='listings'),
]