from django import forms

class staffRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # Forms field with different validation

        # CharField
    name2 = forms.CharField(min_length=5, max_length=15, strip=False)
    name3 = forms.CharField(strip=False)    # strip removes whitespaces if TRUE
    name4 = forms.CharField(empty_value='empty')
    name4 = forms.CharField(error_messages={'required':'Enter your name mf'})

        # BooleanField
    agree = forms.BooleanField(label_suffix='',label='I Agree')

        # IntegerField
    roll = forms.IntegerField(min_value=10,max_value=50)

        # DecimalField
    price = forms.DecimalField(min_value=3, max_value=10, max_digits=2, decimal_places=1)

        # FloatField()
    rate = forms.FloatField(min_value=2, max_value=100)

        # SlugField
    comment = forms.SlugField()

        # URLField
    website = forms.URLField()
    
        # Textarea
    description = forms.CharField(widget=forms.Textarea)

        # TextInput with CSS
    feedback = forms.CharField(min_length=10,max_length=100,widget=forms.TextInput(attrs={'class':'css1 css2','id':'uniqueid'}))

        # Textarea with rows cols
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))