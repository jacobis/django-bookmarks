import settings

from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

# Project
from bookmarks.views import *


urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),

    # auth
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'registration/password_change.html', }),
    (r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),

    # register
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),

    (r'^save/$', bookmark_save_page),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^assets/(?P<path>.*)$', 'serve'),
    )