from django.shortcuts import render
from cards.models import Card
from django.views.generic import (
    ListView,

)


def card_list(request):
    cards = Card.objects.all()
    return render(
        request=request,
        template_name='cards/card_list.html',
        context={
            'card_list': cards
        }
    )


#  widok klasowy - analogicznie do powyzszego
class CardListView(ListView):
    model = Card
