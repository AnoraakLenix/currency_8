from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Rate, ContactUs


def rate_list(request):
    context = {'rate_list': Rate.objects.all()}

    return render(request, 'rate_list.html', context=context)


def contact_list(request):
    context = {"contacts_list": ContactUs.objects.all()}

    return render(request, "contactus_list.html", context=context)


def index(request):
    return render(request, 'index.html')


def http_response(request):
    return HttpResponse('OK')
