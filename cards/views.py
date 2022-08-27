import random

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from cards.forms import CardForm, CardCheckForm
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


class BoxView(CardListView):
    template_name = 'cards/box.html'
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs['box_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        if self.object_list:
            context['check_card'] = random.choice(self.object_list)

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
            card.move(form.cleaned_data['solved'])

        return redirect(request.META.get('HTTP_REFERER'))
