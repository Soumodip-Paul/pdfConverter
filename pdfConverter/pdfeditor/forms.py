from django import forms
from .validators import *

validators = [validate_file_size,validate_file_type]

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'accept': 'application/pdf'}),validators=validators)
    
class CompressFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),validators=validators)
    
class EncryptFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),validators=validators)
    password = forms.CharField(widget=forms.PasswordInput)
