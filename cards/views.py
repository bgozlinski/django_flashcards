from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cards.forms import CardForm
from cards.models import Card
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView

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


def update_view(request, pk):
    card = Card.objects.get(pk=pk)
    form = CardForm(instance=card)
    if request.method == "POST":
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('card-list'))

    return render(
        request=request,
        template_name='cards/card_form.html',
        context={
            'form': form
        }
    )


#  widok klasowy - analogicznie do powyzszego
class CardListView(ListView):
    model = Card
    # ordering = ("box", "-date_created")                       #  ordering przy pomocy atrybutu
    queryset = Card.objects.order_by("box", "-date_created")    #  modyfikacja quesryset


class CardCreateView(SuccessMessageMixin, CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-list")
    success_message = "Karta utworzona!"


class CardUpdateView(CardCreateView, UpdateView, SuccessMessageMixin):
    success_url = reverse_lazy('card-list')
    success_message = 'Karta zauktualzowana'
