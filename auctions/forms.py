from django import forms

from .models import Listing

class ListingForm(forms.ModelForm): 
    class Meta: 
        model = Listing
        fields = ["title", "description", "image", "category"]

        widgets = {
            'description': forms.Textarea()
        }

    def save(self, uid, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

