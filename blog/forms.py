from django import forms
from .models import Podcast, Episode


class PodcastCreateForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
