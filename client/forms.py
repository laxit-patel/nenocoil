from django import forms
from django.forms import TextInput
from client.models import Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import PrependedText, Div
from modules.key_generator import key_generator


class New_Client_Form(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Client_Id', 'Client_Name', 'Client_Address', 'Client_Gstin', 'Client_Email', 'Client_Phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['Client_Id'].initial = key_generator('Client')

        self.helper.layout = Layout(
            Field('Client_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            Field('Client_Name', css_class='w-100 form-control', wrapper_class='form-group'),
            Field('Client_Email', css_class='w-100 form-control', wrapper_class='form-group'),
            Field('Client_Gstin', css_class='w-100 form-control', wrapper_class='form-group'),
            Field('Client_Phone', css_class='w-100 form-control', wrapper_class='form-group'),
            Field('Client_Address', css_class='w-100 form-control', wrapper_class='form-group'),
            Submit('submit', 'Add', css_class='btn btn-block btn-outline-dark'),
        )
