from django import forms

class VaccineForm(forms.Form):
   pin_code = forms.CharField(max_length = 50)
   date = forms.CharField(max_length=50)