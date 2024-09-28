from django import forms

from .models import Listing

class ListingForm(forms.ModelForm): 

    class Meta: 
        model = Listing
        fields = ["title", "description", "starting_bid", "image", "category"]

        widgets = {
            'description': forms.Textarea(),
            'image': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }

    def save(self, uid, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
    
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['starting_bid'].label = "Starting Bid"



