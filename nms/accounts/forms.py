from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.forms.utils import ErrorList


class UserCreateForm(UserCreationForm):
    class_name = forms.CharField()
    instructor = forms.CharField()
    organization = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Wichita, SUU, etc..'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2')
        help_texts = {
            'username': '',
            'email': '',
        }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = 'Verify Password'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
