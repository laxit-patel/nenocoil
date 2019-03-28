from django import forms
from django.forms import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button
from crispy_forms.bootstrap import PrependedText, Div
from reservoir.key_generator import key_generator
from drawing.models import Drawing


class New_Drawing_Form(forms.ModelForm):

    class Meta:
        model = Drawing
        fields = ('Drawing_Id', 'Drawing_File', 'Drawing_Revision', 'Drawing_Origin')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.fields['Drawing_Id'].initial = key_generator('Drawing')
        self.fields['Drawing_File'].required = False

        self.helper.layout = Layout(
            Field('Drawing_Id', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            Field('Drawing_File', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            Field('Drawing_Revision', css_class='w-100 form-control text-dark', wrapper_class='form-group', ),
            HTML("<div class='row'>"),
            HTML("<div class='col-md-9'>"),
            Field('Drawing_Origin', css_class='w-100 form-control text-dark custom-select',
                  wrapper_class='form-group', ),
            HTML("</div>"),
            HTML("<div class='col-md-3'>"),
            HTML("<div class='form-group control-group'>"),
            HTML("<label for='add_new_design'>&nbsp</label>"),
            HTML("<a href='/drawing/add_new_client'>"),
            Button('add_new_drawing', 'add', css_class='material-icons form-control text-white bg-success', ),
            HTML("</a>"),
            HTML("</div>"),
            HTML("</div>"),
            HTML("</div>"),
            Submit('submit', 'Add & Exit', css_class='btn btn-block btn-outline-dark'),
        )