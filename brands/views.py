from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class BrandListView(LoginRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'
    paginate_by = 5


    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs

class BrandCreate(LoginRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')

class BrandDetail(LoginRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_details.html'
    context_object_name = 'brand'

class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')
    context_object_name = 'update'

class BrandDelete(LoginRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')