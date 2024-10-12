from django.shortcuts import render, redirect
from jobs.models import Job
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from django.core.exceptions import PermissionDenied

def jobOffers(request):
    jobs = Job.objects.all()
    return render(request, "jobs/jobs_list.html", context={'jobs': jobs})

def jobDetails(request, id):
    details = Job.objects.get(pk=id)
    return render(request, "jobs/job_details.html", context={'offer': details})

@login_required
def yourOffers(request):
    offers = Job.objects.filter(employer=request.user)
    return render(request, "jobs/your_offers.html", context={'jobs': offers})

@login_required
def add(request):
    form = JobForm()

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            offers = form.save(commit=False)
            offers.employer = request.user
            offers.save()
            return redirect('your_offers')

    context = {'form': form}
    return render(request, "jobs/add_edit.html", context)

@login_required
def edit(request, id):
    offer = Job.objects.get(pk=id)
    form = JobForm(instance=offer)

    if request.method == "POST":
        form = JobForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('your_offers')

    context = {'form': form, 'edit': True, 'id': id}
    return render(request, "jobs/add_edit.html", context)


@login_required
def delete(request, id):
    if request.method == "POST":
        offer = Job.objects.get(pk=id)
        offer.delete()
        return redirect('your_offers')
    return render(request, "jobs/confirm_delete.html")