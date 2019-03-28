from django import forms
from django.forms import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button, Div
from crispy_forms.bootstrap import PrependedText, Div
from modules.key_generator import key_generator
from design.models import Design


class New_Design_Form(forms.ModelForm):

    class Meta:
        model = Design
        fields = (
            'Design_Id',
            'Design_Dimension',
            'Design_Connection',
            'Design_Fpi',
            'Design_Tube',
            'Design_Hairpin',
            'Design_Drawing',
            'Design_Revision',
            'Design_Origin')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['Design_Id'].initial = key_generator('Design')


        self.helper.layout = Layout(
            Div(
                Div(
                    Field('Design_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                Div(
                    Field('Design_Dimension', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-8"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    Field('Design_Connection', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                Div(
                    Field('Design_Fpi', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                Div(
                    Field('Design_Tube', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    Field('Design_Hairpin', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                Div(
                    Field('Design_Revision', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                Div(
                    Field('Design_Drawing', css_class='w-100 form-control text-dark ', wrapper_class='form-group', ),
                    css_class="col-md-4"
                ),
                css_class="row"
            ),
            Div(
                Div(
                    Field('Design_Origin', css_class='w-100 form-control text-dark custom-select', wrapper_class='form-group', ),
                    css_class="col-md-8"
                ),
                Div(
                    HTML("<label for='submit'>&nbsp</label>"),
                    Submit('submit', 'Add', css_class='btn btn-block btn-outline-success text-white'),
                    css_class="col-md-4"
                ),
                css_class="row"
            ),


        )