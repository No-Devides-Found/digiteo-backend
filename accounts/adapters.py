from allauth.account.adapter import DefaultAccountAdapter
import re
from django.forms import ValidationError


class CustomAccountAdapter(DefaultAccountAdapter):
    def clean_password(self, password, user=None):
        # 최소 8 자, 하나 이상의 문자와 하나 이상의 숫자 정규식
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            return password
        else:
            raise ValidationError("Error message")
