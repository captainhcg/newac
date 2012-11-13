from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newac.views.home', name='home'),
    # url(r'^newac/', include('newac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newac.views.index'),
    url(r'^coming/', 'newac.views.coming'),
    url(r'^guest/', 'newac.views.guest'),
    url(r'^leave/', 'newac.views.leave'),
)

print STATIC_ROOT
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
        # (r'^media/(?P<path>.*)/?$', 'django.views.static.serve'),
    )
