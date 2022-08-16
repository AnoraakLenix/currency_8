from django.http import HttpResponse

from currency.models import Rate, ContactUs


def rate_list(request):

    rates_list = []
    for rate in Rate.objects.all():
        html_string = f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy} <br>'
        rates_list.append(html_string)

    return HttpResponse(str(rates_list))


def contact_list(request):

    contacts_list = []
    for contact in ContactUs.objects.all():
        html_string = f'ID: {contact.id}, email_from: {contact.email_from}, email_to: {contact.email_to},' \
                      f'subject: {contact.subject}, message: {contact.message} <br>'
        contacts_list.append(html_string)

    return HttpResponse(str(contacts_list))
