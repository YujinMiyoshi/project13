from django.contrib.auth.forms import AuthenticationForm
from django import forms
from.models import ToDo

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        exclude = ('created_at', 'updated_at',)

