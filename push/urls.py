from django.conf.urls import patterns, url, include

from .views import PushApplication

urlpatterns = [
    url(r'details/', PushApplication.as_view(), name='details'),
]
