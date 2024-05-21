from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')

