from django import forms

from .models import Tweet
class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet # Powiązany model
        fields = ['content'] # Pola z modelu
