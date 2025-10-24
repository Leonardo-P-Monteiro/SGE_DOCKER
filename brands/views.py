from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms

class BrandListView(ListView):
    model = models.Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs

class BrandCreate(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')

