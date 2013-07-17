from django.conf.urls import patterns, include, url
from Remote_Software.views import *
from Remote_Software.Development.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
    url(r'^Remote_Software_Development/$', Remote_Software_Development),
    url(r'^Submitted_Code/$', Submitted_code),
    url(r'^hello_pdf/$', hello_pdf),
    # Examples:
    # url(r'^$', 'Remote_Software.views.home', name='home'),
    # url(r'^Remote_Software/', include('Remote_Software.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)