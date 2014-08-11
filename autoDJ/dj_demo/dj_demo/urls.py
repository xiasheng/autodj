
from django.conf.urls import patterns, include, url

from views.helloworld import hello

urlpatterns = patterns('',

    url(r'^hello/$', hello),

)
