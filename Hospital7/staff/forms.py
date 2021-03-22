from django import forms

class RegisterStaff(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix='--', initial='My name', required=False,
                            disabled=True, help_text='70 characters allowed!')