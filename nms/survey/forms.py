from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

# SURVEY FORMS.PY


class UserCreateForm(UserCreationForm):
    class_name = forms.CharField(label='Class Name')
    instructor = forms.CharField(label='Instructor')
    organization = forms.CharField(label='Organization', widget=forms.TextInput(
        attrs={'placeholder': 'Wichita, SUU, etc...'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(self, UserCreateForm).save(commit=False)
        user.class_name = self.cleaned_data['class_name']
        user.instructor = self.cleaned_data['instructor']
        user.organization = self.cleaned_data['organization']

        if commit:
            user.save()
        return user
