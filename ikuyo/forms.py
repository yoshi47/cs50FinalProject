from dataclasses import fields

from django import forms

from ikuyo.models import LogModel


class TravelEstimateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    class Meta:
        model = LogModel
        fields = ('start', 'goal', 'people', 'days',)