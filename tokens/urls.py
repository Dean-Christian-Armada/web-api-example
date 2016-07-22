from django.conf.urls import include, url

from rest_framework.authtoken.views import ObtainAuthToken

# To add description on DRF Docs
class ObtainAuthToken(ObtainAuthToken):
	"""
	An endpoint to get your token using your username and password that should be provided to you in the e-mail.... Example: {"username":"dean", "password":"armada"}
	"""


urlpatterns = [
	url(r'^$', ObtainAuthToken.as_view()),
]