# -*- coding: utf-8 -*-
#

from django import forms
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=100)
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput,
        max_length=1024, strip=False
    )

    def confirm_login_allowed(self, user):
        if not user.is_staff:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )


class UserLoginCaptchaForm(UserLoginForm):
    captcha = CaptchaField()


class UserCheckOtpCodeForm(forms.Form):
    otp_code = forms.CharField(label=_('MFA code'), max_length=6)
