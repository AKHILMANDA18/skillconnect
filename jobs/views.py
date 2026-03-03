from django.shortcuts import render

def post_job(request):
    return render(request, 'post_job.html')