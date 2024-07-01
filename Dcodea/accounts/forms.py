from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    userPosition = forms.ChoiceField(choices=CustomUser.POSITION_CHOICES, label='Position', required=True)
    userOpen = forms.BooleanField(label='Open', required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'userPosition', 'userOpen']
        # 추가적인 필드 설정이나 초기화 작업을 수행할 수 있습니다.