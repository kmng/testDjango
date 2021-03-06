from django.conf.urls.defaults import *
from project1 import settings

urlpatterns = patterns('project1.accounts.views',
    (r'^register/$', 'register', 
        {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL }, 'register'),
    (r'^my_account/$', 'my_account', 
         {'template_name': 'registration/my_account.html'}, 'my_account'),
    (r'^order_info/$', 'order_info', 
         {'template_name': 'registration/order_info.html'}, 'order_info'),
    (r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details', 
         {'template_name': 'registration/order_details.html'}, 'order_details'),
)

urlpatterns = patterns('project1.accounts.views',
    (r'^register/$', 'register', 
        {'template_name': 'registration/register.html'}, 'register'),
        (r'^my_account/$', 'my_account', 
         {'template_name': 'registration/my_account.html'}, 'my_account'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login/$', 'login', 
     {'template_name': 'registration/login.html' }, 'login'),
)
