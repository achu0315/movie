from django import forms
from . models import film

class movieform(forms.ModelForm):
    class Meta:
        model=film
        fields=['name','dec','year','img']