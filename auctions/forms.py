from django import forms

from .models import Listing

class ListingForm(forms.ModelForm): 
    class Meta: 
        model = Listing 
        fields = "__all__"
    
    def __init__(self):
        super(ListingForm, self).__init__()

        self.fields['seller'].widget = forms.HiddenInput()
        self.fields['active'].widget = forms.HiddenInput()
        self.fields['description'].widget = forms.Textarea()

    def save(self, commit=True):
        instance = super().save(commit=False)

        user = self.request.user
        instance.seller = user

        instance.active = True 

        if commit:
            instance.save()

        # return instance
