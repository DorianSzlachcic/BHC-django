from django.shortcuts import render
from jobs.models import Job

def jobOffers(request):
    jobs = Job.objects.all()
    return render(request, "jobs/jobs_list.html", context={'jobs': jobs})