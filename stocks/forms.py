from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker



class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password2'].label = "Password"

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'founded', 'address1', 'city', 'description',
                  'funding', 'url', 'category', 'image']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        widgets = {'user': forms.HiddenInput(),
                   'post': forms.HiddenInput()}

    # def save(self, commit=True):
    #     # send email stuff
    #     return super(ModelForm, self).save(commit=True)


class FundingForm(ModelForm):
    class Meta:
        model = FundingRound
        widgets = {'company': forms.HiddenInput()}
        fields = ['series', 'raised', 'date', 'company']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'about', 'image']