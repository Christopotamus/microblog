from django.conf.urls.defaults import patterns, include, url
from microblogapp.views import *


# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblogapp.views.home', name='home'),
    # url(r'^microblogapp/', include('microblogapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^home/', home),
    url(r'^register/', register),
    url(r'^verify/\d{16,16}$', verify),
    url(r'^login/', login),
    url(r'^logout/', logout),
)
