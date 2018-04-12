from django import forms


class ContractorForm(forms.Form):
    contractor = forms.CharField(label='Contractor name:', max_length=100)
    director = forms.CharField(label='Director name:', max_length=100)
    address = forms.CharField(label='Address:', max_length=100)
    telephone = forms.CharField(label='Telephone:', max_length=11)
    email = forms.EmailField(label='E-mail:', max_length=75)
