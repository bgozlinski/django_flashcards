from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='cards/base.html'), name='home'),
    path('f/', views.card_list, name='card-list'),
    path('', views.CardListView.as_view(), name='card-list'),
    path('new/', views.CardCreateView.as_view(), name='card-create'),
    path('edit/<int:pk>/', views.update_view, name='card-update'),
    path('f/edit/<int:pk>/', views.update_view, name='card-update-f'),
    path('box/<int:box_num>', views.BoxView.as_view(), name='box'),
]
