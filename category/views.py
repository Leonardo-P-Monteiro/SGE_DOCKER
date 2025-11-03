from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs

class CategoryCreate(CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDetail(DetailView):
    model = models.Category
    template_name = 'category_details.html'
    context_object_name = 'category'

class CategoryUpdate(UpdateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    context_object_name = 'update'

class CategoryDelete(DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')