"""student_list_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from students import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),

    url(r'^api/v1/section/$', views.api_section, name='api_section'),
    url(r'^api/v1/section/(?P<pk>[0-9]+)', views.api_section_detail, name='api_section_detail'),
    url(r'^api/v1/students/', views.api_students, name='api_students'),
    # url(r'^api/v1/students/profile/', views.api_students_profile, name='api_students_profile'),
]
