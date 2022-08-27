from django.shortcuts import render
from cards.models import Card


def card_list(request):
    cards = Card.objects.all()
    return render(
        request=request,
        template_name='cards/card_list.html',
        context={
            'card_list': cards
        }
    )
