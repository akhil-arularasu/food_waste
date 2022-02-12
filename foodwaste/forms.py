from django import forms
from django.core import validators
from foodwaste.models import PledgeInfo, OrganicImage

# class SurveyForm(forms.Form):
#     zip_code = forms.CharField(label='Enter your Zip Code')
#     trash_bag_per_week = forms.IntegerField(label='bags')
#     organic_pct = forms.FloatField(label='Organic %')

def clean(self):
    all_clean_data = super().clean()

class PledgeForm(forms.ModelForm):
#    email = forms.CharField(blank=True)
    class Meta():
        model = PledgeInfo
        fields = ('zip_code', 'state','country', 'total_waste_per_week', 'total_food_waste_per_week', 'pledged_reduction')

class ClassifyForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = OrganicImage
        fields = ('image',) 
