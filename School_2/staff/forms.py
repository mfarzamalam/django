from django import forms

class staffRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

        # Custom validation for single field
    # def clean_name(self):
    #     clean_name_data = self.cleaned_data['name']

    #     if len(clean_name_data) < 5:
    #         raise forms.ValidationError("Enter more than 5 character")
    #     else:
    #         return clean_name_data


        # Custom validation for whole form
    def clean(self):
        cleaned_data = super().clean()
        cname = self.cleaned_data['name']
        cemail = self.cleaned_data['email']

        if len(cname) < 5:
            raise forms.ValidationError('Name should not be less than or equal to 5')

        if len(cemail) < 15:
            raise forms.ValidationError('Email should not be less than or equal to 15')