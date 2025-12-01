from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class SuppliersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supllier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5
    permission_required = 'supplier.view_supplier'

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs

class SuppliersCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supllier
    template_name = 'suppliers_create.html'
    form_class = forms.SuppliersForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'supplier.create_supplier'

class SuppliersDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supllier
    template_name = 'suppliers_details.html'
    context_object_name = 'suppliers'
    permission_required = 'supplier.view_supplier'

class SuppliersUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supllier
    template_name = 'suppliers_create.html'
    form_class = forms.SuppliersForm
    success_url = reverse_lazy('suppliers_list')
    context_object_name = 'update'
    permission_required = 'supplier.change_supplier'

class SuppliersDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supllier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'supplier.delete_supplier'