from django import forms 
from . models import Contact

class ContactUploadForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["first_name","last_name", "surname","phone","email"]