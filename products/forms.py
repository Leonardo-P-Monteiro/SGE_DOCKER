from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'serie_number', 'cost_price', \
                  'selling_price', 'description']
        widgets = {
            'title':forms.TextInput({'class':'form-control'}),
            'category':forms.Select({'class':'form-control'}),
            'brand':forms.Select({'class':'form-control'}),
            'serie_number':forms.TextInput({'class':'form-control'}),
            'cost_price':forms.NumberInput({'class':'form-control'}),
            'selling_price':forms.NumberInput({'class':'form-control'}),
            'description':forms.Textarea({'class':'form-control', 'rows':3,}),
        }
        labels = {
            'title':'Nome',
            'category':'Categoria',
            'brand':'Marca',
            'serie_number':'Número de série',
            'cost_price':'Preço de custo',
            'selling_price':'Preço de venda',
            'description':'Descrição',
        }