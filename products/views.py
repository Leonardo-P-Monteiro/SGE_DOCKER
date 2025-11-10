from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
from category.models import Category
from brands.models import Brand

class ProductListView(ListView):
    model = models.Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 5

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
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()


        return context

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