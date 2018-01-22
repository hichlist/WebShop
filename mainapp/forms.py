from django import forms
from .models import Contact


# class ContactForm(forms.Form):
#     sender = forms.EmailField(label='Email', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     subject = forms.CharField(label='Title', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
#     message = forms.CharField(label='Message', required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('sender', 'subject', 'message')
