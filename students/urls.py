from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.api_students, name='api_students'),
    url(r'^(?P<pk>[0-9]+)', views.api_students_detail, name='api_students'),
]