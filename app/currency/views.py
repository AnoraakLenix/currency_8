from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views import generic
from django.urls import reverse_lazy
from currency.models import Rate, Source
from currency.forms import RateForm, SourceForm


class RateListView(generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

class RateDetailsView(generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


class SourceListView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/source_list.html'


class SourceDetailsView(generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'currency/source_details.html'


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source_list')

