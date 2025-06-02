from django.shortcuts import get_object_or_404, redirect
from eshop.models import Produkt

def delete(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)
    produkt.delete()
    return redirect('produkty_seznam')
