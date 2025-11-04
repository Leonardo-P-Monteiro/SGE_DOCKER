from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            qs = qs.filter(product__title__icontains=product)

        return qs

class OutflowCreate(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')

class OutflowDetail(DetailView):
    model = models.Outflow
    template_name = 'outflow_details.html'
    context_object_name = 'outflow'