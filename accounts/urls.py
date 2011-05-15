from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from accounts.views import *


urlpatterns = patterns('',
    # Signup, signin and signout
    url(r'^signup/$', signup, name='accounts_signup'),
    #url(r'^signin/$', signin, name='accounts_signin'),
    #url(r'^signout/$', auth_views.logout, {'template_name': 'accounts/signout.html'}, name='accounts_signout'),
    url(r'^(?P<username>[\.\w]+)/signup/complete/$', direct_to_user_template, {'template_name': 'accounts/signup_complete.html'}, name='accounts_signup_complete'),


)
