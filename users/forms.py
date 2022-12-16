from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile
from django import forms
class AdminCreate(UserCreationForm) :
    class Meta :
        model = User
        fields = ["username", "password1", "password2"]


class UpdateInfo(forms.ModelForm) :
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta :
        model = User
        fields = [ 
            "username",
            "first_name", 
            "last_name",
            "email",
            "date_of_birth",
            "gender",
        ]

    
        


class UserCreateProfile(UserCreationForm) :
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"calss":"form-control"}))
    class Meta :
        model = User
        fields = [ 
            "username",
            "email",
            'gender',
            "date_of_birth",
            "password1",
            "password2",
        ]
    def clean_email(self) :
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists() :
            raise forms.ValidationError("this email already to used ")
        return email
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        # self.fields['password2'].label = ''
        # self.fields['gender'].label = ''
        # self.fields['date_of_birth'].label = ''
        # self.fields['email'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password1'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})
        self.fields['password2'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password confirmation", 'data-toggle': 'password'})
        self.fields['email'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Email"})
        self.fields['gender'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Gender"})
        self.fields['date_of_birth'].widget.attrs.update({"placeholder":"Select date","class":"form-control" })
   
class LoginForm(AuthenticationForm) :
    class Meta :
        model = User
        fields = [ 
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['username'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Username"})
        self.fields['password'].widget.attrs.update({'class':"form-control","id":"exampleInputEmail1","placeholder":"Password", "data-toggle":"password"})
        

class UpdateProfileForm(forms.ModelForm) :
    username = forms.CharField()
    class Meta :
        model = Profile
        fields = [ 
            'username',
            'bio',
            'avatar',
            'nationality'
        ]