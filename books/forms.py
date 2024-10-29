
from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(label='Ism')
    email = forms.EmailField(label='Qabul qiluvchi emaili',widget=forms.EmailInput)
    comments = forms.CharField(label='Izohlar', widget=forms.Textarea)