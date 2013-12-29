from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static

# Project
from bookmarks.views import *


urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^assets/(?P<path>.*)$', 'serve'),
    )