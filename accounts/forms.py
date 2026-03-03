from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help text
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        # Add placeholders
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })