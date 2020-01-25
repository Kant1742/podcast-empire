from django import forms
from .models import Podcast, Episode


class PodcastCreateForm(forms.Form):
    class Meta:
        model = Podcast
