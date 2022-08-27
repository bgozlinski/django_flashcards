from django.shortcuts import render
from django.urls import reverse_lazy
from cards.models import Card
from django.views.generic import (
    ListView, CreateView,

)


def card_list(request):
    cards = Card.objects.all().order_by("box", "-date_created")  # all jest tu zbędne
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
    # ordering = ("box", "-date_created")                       #  ordering przy pomocy atrybutu
    queryset = Card.objects.order_by("box", "-date_created")    #  modyfikacja quesryset


class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('card-create')
