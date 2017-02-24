from django.conf.urls import url
from django.contrib import admin
from .views import HomeTemplateView,AboutTemplateView,register_view,contact_view

urlpatterns = [
	# url(r'^create$', views.home, name="create"),
	url(r'^$', HomeTemplateView.as_view(), name="home"),
	url(r'^about/$', AboutTemplateView.as_view(), name="about"),
	url(r'^contact/$', contact_view, name="contact"),
	url(r'^register/$', register_view, name="register"),


]
