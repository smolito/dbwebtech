from django.shortcuts import render
from eshop.forms.uzivatele.nick_form import NickForm


def set_nick(request):
    form = NickForm(request.POST or None)

    context = {
        'formular': form,
    }

    if request.method == 'POST' and form.is_valid():
        nick = form.cleaned_data['username']
        request.session['nick'] = nick

    context['nick'] = request.session.get('nick', None)

    return render(request, 'uzivatele/nick_zmenit.html', context)
