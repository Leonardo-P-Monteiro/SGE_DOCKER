from django.views.generic import ListView
from . import models

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

