from django import forms
from .models import Todo, UserProfile

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['input_field']

class IntroductionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['introduction']