from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.defaults import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xxSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


from New.views import *
urlpatterns = patterns('',
(r'^$', main_page),
)