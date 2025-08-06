from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Client
from .models import Battery  # импорт модели батарей


def index(request):
    return render(request, 'core/index.html')

def clients_list(request):
    clients = Client.objects.all().order_by('created_at')
    return render(request, 'core/clients_list.html', {'clients': clients})

@staff_member_required  # гарантирует доступ только админам и интеграцию с админкой
def battery_list(request):
    batteries = Battery.objects.all()
    return render(request, 'core/battery_list.html', {'batteries': batteries})


