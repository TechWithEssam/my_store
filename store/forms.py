from .models import *
from django import forms
from accounts.models import Account
from django.db.models import Q
class AddNewCategory(forms.ModelForm) :
    class Meta :
        model = Category
        fields = ("name",)

class AddBrandForm(forms.ModelForm) :
    class Meta :
        model = Brand
        fields = "name",


class AddNewProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = [ 
            "name",
            "image",
            "price",
            "category",
            "brand",
            "description",
            "option",
            "discount",
        ]
    
    def clean_description(self) :
        description = self.cleaned_data.get("description")
        if len(description) < 10 :
            raise forms.ValidationError("Description must not be less than 100 characters")
        return  description
    
    
        