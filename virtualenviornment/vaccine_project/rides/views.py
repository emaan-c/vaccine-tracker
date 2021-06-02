from django.shortcuts import render, redirect
from .forms import UberInformationForm
from .models import UberInformation
from django.views.generic import TemplateView
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

def get_ride_info(request):
    UberInformation.objects.all().delete()
    context = {}
    if request.method == 'POST':
        form = UberInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uber-main')
    else:
        form = UberInformationForm()
    context['form'] = form
    return render(request, 'rides/ride_main.html', context)

class UberView(TemplateView):
    template_name = 'rides/uber.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fs"] = UberInformation.objects.all()

        return context