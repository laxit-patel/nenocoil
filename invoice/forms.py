from django import forms
from .models import Invoice
from order.models import Order
from client.models import Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


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
        fields = ('Invoice_Id', 'Invoice_Client', 'Invoice_Order')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'Invoice_Id',
            'Invoice_Client',
            Submit('submit', 'Generate', css_class='btn btn-success')
        )


class Pre_Invoice(forms.Form):

    Invoice_Client = forms.ModelChoiceField(queryset=Client.objects.all().values_list())
    Invoice_Order = forms.ModelChoiceField(queryset=Order.objects.all().values_list())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
