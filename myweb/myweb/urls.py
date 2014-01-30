from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
  url(r'^',include('apple3.urls')),
    # url(r'^myweb/', include('myweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/',include('registration.backends.default.urls')),
    #url(r'^accounts/login/$','myweb.views.login'),
    #url(r'^accounts/auth/$','myweb.views.auth_view'),
    #url(r'^accounts/logout/$','myweb.views.logout'),
    #url(r'^accounts/loggedin/$','myweb.views.loggedin'),
    #url(r'^accounts/invalid_login/$','myweb.views.invalid_login'),

#    url(r'^accounts/register_success/$','myweb.views.register_success'),
 #   url(r'^accounts/register/$','myweb.views.register_user'),
)
