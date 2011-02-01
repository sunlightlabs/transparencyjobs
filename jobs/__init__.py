from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def on_submit_email(job):
    
    subject = "Thank you for posting your job!"
    body = render_to_string("email/jobsubmit.txt", {"job": job})
    from_email = "bot@transparencyjobs.com"
    to = [job.contact_email]
    headers = {'Reply-To': 'bounce@transparencyjobs.com'}
    
    email = EmailMessage(subject, body, from_email, to, headers=headers)
    email.send(fail_silently=True)

def on_moderation_email(mo):
    
    if mo.status == 1:
        
        job = mo.content_object
    
        subject = "Your job listing has been %s" % mo.get_status_display().lower()
        
        if mo.status == 1:
            body = render_to_string("email/job_approved.txt", {"job": job})
        else:
            body = render_to_string("email/job_rejected.txt", {"job": job})
            
        from_email = "bot@transparencyjobs.com"
        to = [job.contact_email]
        headers = {'Reply-To': 'bounce@transparencyjobs.com'}
    
        email = EmailMessage(subject, body, from_email, to, headers=headers)
        email.send(fail_silently=True)