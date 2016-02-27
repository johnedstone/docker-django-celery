from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from photos.views import PhotoView
from feedback.views import FeedbackView
from bsub.urls import router

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name="home"),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]
