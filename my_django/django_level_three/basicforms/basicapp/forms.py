from django import forms
from django.core import validators

class FormName (forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
 