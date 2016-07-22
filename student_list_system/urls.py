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

# from students import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.home, name='home'),

    # url(r'^api/sections/$', views.api_section, name='api_section'),
    # url(r'^api/section/(?P<pk>[0-9]+)', views.api_section_detail, name='api_section_detail'),
    # url(r'^api/students/', views.api_students, name='api_students'),
    # url(r'^api/section/(?P<pk>[0-9]+)', views.api_students, name='api_students'),
    # url(r'^api/v1/students/profile/', views.api_students_profile, name='api_students_profile'),
    # Returns the token when a username and password is requested
    # Source: http://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint
    # Example: {"username":"xxx", "password":"xyz"} to http://127.0.0.1:8000/api-token-auth/
    url(r'^tokens/', include('tokens.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^sections/', include('sections.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
