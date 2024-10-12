from django.shortcuts import render
from jobs.models import Job

def jobOffers(request):
    jobs = Job.objects.all()
    return render(request, "jobs/jobs_list.html", context={'jobs': jobs})

def jobDetails(request, id):
    details = Job.objects.get(pk=id)
    return render(request, "jobs/job_details.html", context={'offer': details})