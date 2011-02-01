from django.conf.urls.defaults import *
from transparencyjobs.jobs.feeds import LatestJobs

feeds = {
    'latest': LatestJobs,
}

urlpatterns = patterns('',
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name="job_feed"),
)

urlpatterns += patterns('transparencyjobs.jobs.views',
    url(r'^add/preview/', 'joblisting_preview', name="job_preview"),
    url(r'^add/thanks/', 'joblisting_thanks', name="job_thanks"),
    url(r'^add/', 'joblisting_add', name="job_add"),
    url(r'^(?P<object_id>\d+)/', 'joblisting_detail', name="job_detail"),
    url(r'^$', 'joblisting_list', name="job_list"),
)