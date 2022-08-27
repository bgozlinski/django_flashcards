from import_export import resources
from cards.models import Card
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


class CardResource(resources.ModelResource):

    class Meta:
        model = Card
        fields = ('question', 'answer', 'box',)


class CardAdmin(ImportExportModelAdmin):
    resource_class = CardResource


admin.site.register(Card, CardAdmin)
