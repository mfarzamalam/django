from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class AboutForm(forms.Form):
    
    your_name = forms.CharField()
    your_email = forms.EmailField()
    your_message = forms.CharField(widget=forms.Textarea)