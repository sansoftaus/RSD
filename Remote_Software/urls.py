from django.conf.urls import patterns, include, url
from Remote_Software.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^hello/$', hello),
    # Examples:
    # url(r'^$', 'Remote_Software.views.home', name='home'),
    # url(r'^Remote_Software/', include('Remote_Software.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
