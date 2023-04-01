from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'accept': 'application/pdf'}))
class CompressFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}))
class EncryptFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}))
    password = forms.CharField(widget=forms.PasswordInput)