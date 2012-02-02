from django.conf.urls.defaults import patterns, include, url
from microblogapp.views import *
from microblogapp.pages import *


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
    url(r'^verify/[a-zA-Z0-9]{16,16}/$', verify_noform),
    url(r'^verify/', verify),
    url(r'^login/', login),
    url(r'^logout/', logout),
    
    #ajax get/new post functions
    url(r'^getmainwuphfs/', get_main_wuphfs),
    url(r'^postnewwuphf/', post_new_wuphf),
)
