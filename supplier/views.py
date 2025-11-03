from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

class SuppliersListView(ListView):
    model = models.Supllier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs

class SuppliersCreate(CreateView):
    model = models.Supllier
    template_name = 'suppliers_create.html'
    form_class = forms.SuppliersForm
    success_url = reverse_lazy('suppliers_list')

class SuppliersDetail(DetailView):
    model = models.Supllier
    template_name = 'suppliers_details.html'
    context_object_name = 'suppliers'

class SuppliersUpdate(UpdateView):
    model = models.Supllier
    template_name = 'suppliers_create.html'
    form_class = forms.SuppliersForm
    success_url = reverse_lazy('suppliers_list')
    context_object_name = 'update'

class SuppliersDelete(DeleteView):
    model = models.Supllier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('suppliers_list')