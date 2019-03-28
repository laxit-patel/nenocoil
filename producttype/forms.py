from django import forms
from django.forms import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button
from crispy_forms.bootstrap import PrependedText, Div
from reservoir.key_generator import key_generator
from .models import ProductType


class New_ProductType_Form(forms.ModelForm):

    class Meta:
        model = ProductType
        fields = ('ProductType_Id', 'Product_Type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['ProductType_Id'].initial = key_generator('ProductType')
        self.fields['Product_Type'].queryset = ProductType.objects.values('Product_Type')

        self.helper.layout = Layout(
            Field('ProductType_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            Field('Product_Type', css_class='w-100 form-control', wrapper_class='form-group'),
            Submit('submit', 'Add & Exit', css_class='btn btn-block btn-outline-dark'),
        )
