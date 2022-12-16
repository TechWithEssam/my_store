from django import forms
from .models import Account


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'email', 'Brief','address', 'town', 'county',
        'country', 'longitude', 'latitude', 'logo')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of Your Page'
        self.fields['email'].label = 'Email'
        self.fields['Brief'].label = 'Brief of Your page'
        self.fields['address'].label = 'Address'
        self.fields['town'].label = 'Town'
        self.fields['county'].label = 'County'
        self.fields['country'].label = 'Country'
        self.fields['longitude'].label = 'Longitude'
        self.fields['latitude'].label = 'Latitude'
        self.fields['logo'].label = 'Logo'