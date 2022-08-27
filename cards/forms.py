from django.forms import ModelForm
from cards.models import Card
from django import forms


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'box']


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
