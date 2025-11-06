from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

class ProductListView(ListView):
    model = models.Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            qs = qs.filter(title__icontains=title)

        return qs

class ProductCreate(CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'product_details.html'
    context_object_name = 'product'

class ProductUpdate(UpdateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    context_object_name = 'update'

class ProductDelete(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')