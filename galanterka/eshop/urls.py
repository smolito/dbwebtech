from django.urls import path
from eshop.views.produkty.index import index

urlpatterns = [
    path('', index, name='produkty_seznam'),
]
