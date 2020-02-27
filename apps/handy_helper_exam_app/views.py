from django.shortcuts import render, redirect
from .models import Job


# Create your views here.

def index(request):
    return redirect('/dashboard')

def all_jobs(request):
    context = {
        'all_jobs': Job.objects.all()
    }
    return render(request, 'all_jobs.html', context)

def add_job(request):
    return render(request, 'add_job.html')

def create_job(request):
    job = Job.objects.create(
        title = request.POST['title'],
        location = request.POST['location'],
        desc = request.POST['desc'],
    )
    return redirect('/dashboard')

def display_job(request, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'display_job.html', context)

def edit_job(request, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'edit_job.html', context)

def update_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.title = request.POST['title']
    job.desc=request.POST['desc']
    job.location=request.POST['location']
    job.save()

    return redirect('/dashboard')

def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    
    return redirect('/dashboard')



