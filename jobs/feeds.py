from django.contrib.syndication.feeds import Feed
from transparencyjobs.jobs.models import JobListing
import gatekeeper

class LatestJobs(Feed):
    
    title = "Latest jobs from TransparencyJobs.com"
    link = "/jobs/"
    description = "Latest jobs from TransparencyJobs.com"
    
    def ttl(self):
        return '120' # two hour ttl

    def items(self):
        return gatekeeper.approved(JobListing.objects.open())

    def item_author_name(self, job_listing):
        return job_listing.contact_name

    def item_pubdate(self, job_listing):
        return job_listing.date_published