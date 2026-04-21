from django import forms


class NewForm(forms.Form):
    task = forms.CharField(label="label1")
