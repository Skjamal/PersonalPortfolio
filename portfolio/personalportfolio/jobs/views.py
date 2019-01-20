from django.shortcuts import render

# Create your views here.
def satinder(request):
    return render(request, 'jobs/satinder.html')

def home(request):
    return render(request, 'jobs/home.html')