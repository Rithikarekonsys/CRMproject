from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'create.html')


def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'signin.html')

