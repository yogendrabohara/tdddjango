from django.shortcuts import render

# Create your views here.


def drillView(request):
    return render(request, 'drill.html')
