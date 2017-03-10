from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DonationForm
from .models import Donation, CharityFund


def _common_context():
    return {
        'donations': Donation.objects.filter(public=True).order_by('-timestamp'),
        'charity_funds': CharityFund.objects.all(),
    }


def index(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('thanks'))
    context = _common_context()
    context['form'] = form
    return render(request, 'index.html', context)


def thanks(request):
    return render(request, 'thanks.html', _common_context())


def public(request, template_name):
    return render(request, 'public/{}.html'.format(template_name), _common_context())
