from django.shortcuts import render
from main.models import Services, Doctors
# Create your views here.

def indexHandler(request):
    doctors = Doctors.objects.filter(status=0)
    services = Services.objects.filter(status=0)

    return render(request, 'index.html', {
        'doctors' : doctors,
        'services': services
    }
                  )

def index2Handler(request):
    doctors = Doctors.objects.filter(status=0)
    services = Services.objects.filter(status=0)

    return render(request, 'index_2.html', {
        'doctors': doctors,
        'services': services
    }
                  )