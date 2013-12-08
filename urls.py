from django.conf.urls.defaults import patterns, include, url

# Project
from bookmarks.views import *


urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
)
