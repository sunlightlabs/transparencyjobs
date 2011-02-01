from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^jobs/', include('transparencyjobs.jobs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/jobs/'}),
)