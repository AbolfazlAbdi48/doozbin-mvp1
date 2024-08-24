import re

from django import forms


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': '09xxxxxxxxx'
        }),
        help_text='شماره موبایل با 09 شروع شود.',
        label='شماره موبایل',
        min_length=11,
        max_length=11
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        regex = r"^[0-9]{2,}[0-9]$"
        subst = ""
        result = re.sub(regex, subst, phone_number, 0, re.MULTILINE)
        if len(phone_number) != 11 and not result:
            raise forms.ValidationError('لطفا شماره موبایل را به درستی وارد کنید.')
        return phone_number


class VerifyOtpForm(forms.Form):
    code = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'xxxx', 'autofocus': True
        }),
        label='کد تائید',
        min_length=4,
        max_length=4,
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'nickname'
        }),
        label='nickname',
        required=True
    )
    referral_code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'کد معرف'
        }),
        label='کد معرف',
        required=False
    )
