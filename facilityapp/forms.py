from django.forms import ModelForm
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row,Column, HTML
from crispy_forms.bootstrap import Tab, TabHolder

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'
        labels = {
            'floor_area': 'Floor Area m2',
            'site_area': 'Site Area m2',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h3>Facility Form </h3>"
            ),
            Row(
                Column(HTML('<h4>Basic</h4>'),css_class='col-6'),
                Column(HTML("<h4>Area Detail</h4>"), css_class='col-6'),
            ),
            Row(
                Column('facility_name', 'address', 'primary_purpose', css_class='form-group col-md-6'),
                Column('floor_area', 'site_area', css_class='form-group col-md-6')
            ),
            Row(
                Column('length', css_class='form-group col-md-4'),
                Column('width', css_class='form-group col-md-4'),
                Column('height', css_class='form-group col-md-4'),
            ),
            'description',
        )
        self.helper.add_input(Submit('submit', "Submit"))
