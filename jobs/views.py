from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from transparencyjobs.jobs.models import JobListing, JobListingForm, POSITION_TYPE_CHOICES
import gatekeeper

def joblisting_list(request, page=1):
    jobs = gatekeeper.approved(JobListing.objects.open())
    return object_list(request, queryset=jobs, paginate_by=10, template_object_name="job")

def joblisting_detail(request, object_id):
    jobs = gatekeeper.approved(JobListing.objects.filter(pk=object_id))
    other_jobs = gatekeeper.approved(JobListing.objects.open().exclude(pk=object_id).order_by("?"))[:5]
    try:
        return object_detail(request, queryset=jobs, object_id=object_id, template_object_name="job", extra_context={"other_jobs":other_jobs})
    except Http404:
        return HttpResponse("couldn't find job")
        
def joblisting_add(request):
    return HttpResponseRedirect('/')
    # if request.method == 'POST':
    #     form = JobListingForm(request.POST)
    #     if form.is_valid():
    #         if "submit" in request.POST:
    #             form.save()
    #             return HttpResponseRedirect(reverse('job_thanks'))
    # else:
    #     form = JobListingForm()
    # return render_to_response("jobs/joblisting_form.html", {"form": form}, context_instance=RequestContext(request))

def joblisting_preview(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            type_dict = dict(POSITION_TYPE_CHOICES)
            position_type = type_dict.get(form.cleaned_data['position_type'], "Unspecified")
            return render_to_response("jobs/joblisting_preview.html",
                                      {"form": form, "position_type": position_type},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response("jobs/joblisting_form.html",
                                      {"form": form},
                                      context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse('job_list'))

def joblisting_thanks(request):
    return render_to_response("jobs/joblisting_thanks.html")
    