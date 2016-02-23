from django.conf.urls import url
from django.contrib import admin
from frontend.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', Homepage.as_view(), name='home'),
    url(r'^update/$', UpdateBase.as_view(), name='update'),
]
