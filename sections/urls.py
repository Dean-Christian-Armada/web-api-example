from django.conf.urls import include, url

from students import views

urlpatterns = [
	url(r'^$', views.api_section, name='api_section'),
	url(r'^(?P<pk>[0-9]+)', views.api_section_detail, name='api_section_detail'),
]