from django import forms
from django.forms import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button
from crispy_forms.bootstrap import PrependedText, Div
from reservoir.key_generator import key_generator
from product.models import Product


class New_Product_Form(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('Product_Id', 'Product_Design', 'Product_Price', 'Product_Type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['Product_Id'].initial = key_generator('Product')

        self.helper.layout = Layout(
            Field('Product_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            HTML("<div class='row'>"),
            HTML("<div class='col-md-9'>"),
            Field('Product_Design', css_class='w-100 form-control custom-select', wrapper_class='form-group'),
            HTML("</div>"),
            HTML("<div class='col-md-3'>"),
            HTML("<div class='form-group control-group'>"),
            HTML("<label for='add_new_design'>&nbsp</label>"),
            HTML("<a href='add_new_design'>"),
            Button('add_new_design', 'add', css_class='material-icons form-control text-white bg-success',),
            HTML("</a>"),
            HTML("</div>"),
            HTML("</div>"),
            HTML("</div>"),
            Field('Product_Price', css_class='w-100 form-control', wrapper_class='form-group'),
            HTML("<div class='row'>"),
            HTML("<div class='col-md-9'>"),
            Field('Product_Type', css_class='w-100 form-control custom-select', wrapper_class='form-group'),
            HTML("</div>"),
            HTML("<div class='col-md-3'>"),
            HTML("<div class='form-group control-group'>"),
            HTML("<label for='add_new_design'>&nbsp</label>"),
            HTML("<a href='add_new_producttype'>"),
            Button('add_new_producttype', 'add', css_class='material-icons form-control text-white bg-success', ),
            HTML("</a>"),
            HTML("</div>"),
            HTML("</div>"),
            HTML("</div>"),
            Submit('submit', 'Add & Exit', css_class='btn btn-block btn-outline-dark'),
        )