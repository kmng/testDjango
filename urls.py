from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project1/', include('project1.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^accounts/', include('accounts.urls')),    
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^admin/', include(admin.site.urls)),	
    (r'^',include('catalog.urls')),
	(r'^preview/', 'preview.views.home'),
    (r'^cart/',include('cart.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root' :'/home/user/Public/testDjango/project1/static'}),
)
