from django import forms

from .models import Donation



class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'charity_fund', 'amount', 'public']
