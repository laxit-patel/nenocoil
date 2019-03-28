from django import forms
from django.forms import TextInput
from .models import Invoice
from order.models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import PrependedText, Div
from reservoir.key_generator import key_generator


'''
class Generate_Invoice_Form_using_form(forms.Form):
    Invoice_Id = forms.CharField(max_length=50)
    Invoice_Client = forms.CharField(max_length=100, initial="Here Lies Client")
    Invoice_Order = forms.CharField(max_length=50)
    Invoice_Copy_Type = forms.ChoiceField(choices=[('delivery', 'Delivery'), ('supplier', 'Supplier'), ('other', 'Other')])
'''


class Invoice(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('Invoice_Total', 'Invoice_Product')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'Invoice_Id',
            'Invoice_Client',
            Submit('submit', 'Generate', css_class='btn btn-success')
        )



class New_Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('Order_Id', 'Order_Client', 'Order_Amount', 'Order_Date', 'Order_Deadline', 'Order_Reference')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['Order_Id'].initial = key_generator('Order')

        self.helper.layout = Layout(
            HTML("<div class='row'>"),
            Field('Order_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            Field('Order_Client', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-8'),
            HTML("</div>"),
            HTML("<div class='row'>"),
            Field('Order_Date', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            Field('Order_Deadline', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            Field('Order_Reference', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            HTML("</div>"),
            HTML("<div class='row'>"),
            Field('Order_Wages', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            Field('Order_Amount', css_class='w-100 form-control text-dark', wrapper_class='form-group col-md-4'),
            HTML("</div>"),

            Submit('submit', 'Add Order', css_class='btn btn-block btn-outline-dark'),
        )
