from django import forms
from .models import User

class bookdata(forms.ModelForm):
    class Meta:
        model = User
        fields = ['refid','bookname','author','language']
        widgets = {
                'refid':forms.TextInput(attrs={'class':'form-control'}),
                'bookname':forms.TextInput(attrs={'class':'form-control'}),
                'author':forms.TextInput(attrs={'class':'form-control'}),
                'language':forms.TextInput(attrs={'class':'form-control'}),
        }
