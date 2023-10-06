from django import forms
from .models import AdRecord

class AdRecordForm(forms.ModelForm):
    class Meta:
        model = AdRecord
        exclude = ('reimbursement',)  # Exclude the reimbursement field

    AD_TYPE_CHOICES = [
            '0011',
            '1011',
            '1111',
            '1010',
        ]

    ad_type = forms.ChoiceField(choices=[(choice, choice) for choice in AD_TYPE_CHOICES], label='Ad Type', required=True)