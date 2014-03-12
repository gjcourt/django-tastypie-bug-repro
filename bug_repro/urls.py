from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# API                          
from bug_repro.api.views import *   
resources = [                  
    UserResource,
    ForumResource,
]                              
                               
from tastypie.api import Api   
api_v1 = Api(api_name='1')     
for resource in resources:     
    api_v1.register(resource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bug_repro.views.home', name='home'),
    # url(r'^bug_repro/', include('bug_repro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_v1.urls)),
)
