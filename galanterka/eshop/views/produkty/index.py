from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eshop.models import Produkt

def index(request):
    produkty = Produkt.objects.all()
    data_pro_template = {'produkty': produkty}

    nazev_template = 'produkty/index.html'

    # možnost 1
    # template = loader.get_template(nazev_template)
    # return HttpResponse(template.render(data_pro_template, request))

    # možnost 2
    return render(request, nazev_template, data_pro_template)
