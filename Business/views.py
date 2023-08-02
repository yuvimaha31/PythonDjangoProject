from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'business\home.html')

    ### return render(request, 'home.html')