from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from . import serializer
from category.models import Category
from brands.models import Brand
from app.metrics import get_product_metric
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 5
    permission_required = 'products.view_product'

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            qs = qs.filter(title__icontains=title)
        
        if serie_number:
            qs = qs.filter(serie_number__icontains=serie_number)
        
        if category:
            qs = qs.filter(category__id = category)
        
        if brand:
            qs = qs.filter(brand__id = brand)

        return qs
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['product_metrics']= get_product_metric()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()


        return context

class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.create_product'

class ProductDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_details.html'
    context_object_name = 'product'
    permission_required = 'products.view_product'

class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    context_object_name = 'update'
    permission_required = 'products.change_product'

class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'

class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer

