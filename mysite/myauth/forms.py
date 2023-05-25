from django import forms
from .models import Profile


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

    # images = forms.ImageField(widget=forms.ClearableFileInput(), )

