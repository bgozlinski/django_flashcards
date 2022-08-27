import pytest
from django.test import TestCase
from cards.models import Card

@pytest.mark.django_db
class TestModelCard:

    def test_move_method(self):
        c = Card.objects.create(question='house', answer='dom', box=1)
        assert c.box == 1
        c.move(solved=True)
        assert c.box == 2

    def test_str(self):
        c = Card.objects.create(question='house', answer='dom', box=1)
        assert str(c) == 'house'
