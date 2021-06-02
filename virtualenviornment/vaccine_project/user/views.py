from django.shortcuts import render, redirect
from .models import Information, Toronto, Hamilton, Mississauga, Ottawa, Brampton
from .forms import InformationForm
from django.views.generic import TemplateView, DetailView
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def home(request):
    return render(request, 'user/home.html')

def get_info(request):
    Information.objects.all().delete()
    context = {}
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listpharmacy')
    else:
        form = InformationForm()
    context['form'] = form
    return render(request, 'user/user_info.html', context)

class InformationView(TemplateView):
    template_name = 'user/listpharmacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["js"] = Information.objects.all()
        a = Information.objects.order_by('age')[0]
        age = a.age

        if age < '18':
            return context
        
        else:
            s = Information.objects.order_by('street')[0]
            street = s.street
            l = Information.objects.order_by('street')[0]
            location = l.location
            f = street + ', ' + location + ', ' + 'Canada'
            fulladdress = str(f)
            locator = Nominatim(user_agent='myGeocoder')
            locationaire = locator.geocode(fulladdress)
            coordinates_latitude = locationaire.latitude
            coordinates_longitude = locationaire.longitude
            users_coordinates = (coordinates_latitude, coordinates_longitude)

            if location == 'Toronto':

                location1 = (43.7082127, -79.4781558)
                location_1 = round(great_circle(users_coordinates, location1).kilometers,1)
                distance1 = Toronto.objects.all()[0]
                distance1.distance_from_user = location_1
                distance1.save()

                location2 = (43.7022155, -79.5224508)
                location_2 = round(great_circle(users_coordinates, location2).kilometers,1)
                distance2 = Toronto.objects.all()[1]
                distance2.distance_from_user = location_2
                distance2.save()

                location3 = (43.6989823, -79.4755084)
                location_3 = round(great_circle(users_coordinates, location3).kilometers,1)
                distance3 = Toronto.objects.all()[2]
                distance3.distance_from_user = location_3
                distance3.save()

                location4 = (43.7095985, -79.5337277)
                location_4 = round(great_circle(users_coordinates, location4).kilometers,1)
                distance4 = Toronto.objects.all()[3]
                distance4.distance_from_user = location_4
                distance4.save()

                location5 = (43.6661388, -79.3683352)
                location_5 = round(great_circle(users_coordinates, location5).kilometers,1)
                distance5 = Toronto.objects.all()[4]
                distance5.distance_from_user = location_5
                distance5.save()

                location6 = (43.724034, -79.300677)
                location_6 = round(great_circle(users_coordinates, location6).kilometers,1)
                distance6 = Toronto.objects.all()[5]
                distance6.distance_from_user = location_6
                distance6.save()

                location7 = (43.6701586, -79.3756379)
                location_7 = round(great_circle(users_coordinates, location7).kilometers,1)
                distance7 = Toronto.objects.all()[6]
                distance7.distance_from_user = location_7
                distance7.save()

                location8 = (43.6701586, -79.3756379)
                location_8 = round(great_circle(users_coordinates, location8).kilometers,1)
                distance8 = Toronto.objects.all()[7]
                distance8.distance_from_user = location_8
                distance8.save()

                location9 = (43.7082127, -79.4781558)
                location_9 = round(great_circle(users_coordinates, location9).kilometers,1)
                distance9 = Toronto.objects.all()[8]
                distance9.distance_from_user = location_9
                distance9.save()

                context["qs"] = Toronto.objects.all().order_by('distance_from_user')

                return context

            if location == 'Hamilton':

                location1 = (43.2339729, -79.9106616)
                location_1 = round(great_circle(users_coordinates, location1).kilometers,1)
                distance1 = Hamilton.objects.all()[0]
                distance1.distance_from_user = location_1
                distance1.save()

                location2 = (43.1952799, -79.8627461)
                location_2 = round(great_circle(users_coordinates, location2).kilometers,1)
                distance2 = Hamilton.objects.all()[1]
                distance2.distance_from_user = location_2
                distance2.save()

                location3 = (43.2370533, -79.8772574)
                location_3 = round(great_circle(users_coordinates, location3).kilometers,1)
                distance3 = Hamilton.objects.all()[2]
                distance3.distance_from_user = location_3
                distance3.save()

                location4 = (43.2057906, -79.8648585)
                location_4 = round(great_circle(users_coordinates, location4).kilometers,1)
                distance4 = Hamilton.objects.all()[3]
                distance4.distance_from_user = location_4
                distance4.save()

                context["qs"] = Hamilton.objects.all().order_by('distance_from_user')

                return context

            if location == 'Mississauga':

                location1 = (43.6103032, -79.5759717)
                location_1 = round(great_circle(users_coordinates, location1).kilometers,1)
                distance1 = Mississauga.objects.all()[0]
                distance1.distance_from_user = location_1
                distance1.save()

                location2 = (43.521047, -79.6889729)
                location_2 = round(great_circle(users_coordinates, location2).kilometers,1)
                distance2 = Mississauga.objects.all()[1]
                distance2.distance_from_user = location_2
                distance2.save()

                location3 = (43.6121428, -79.6903758)
                location_3 = round(great_circle(users_coordinates, location3).kilometers,1)
                distance3 = Mississauga.objects.all()[2]
                distance3.distance_from_user = location_3
                distance3.save()

                location4 = (43.562699, -79.6511316)
                location_4 = round(great_circle(users_coordinates, location4).kilometers,1)
                distance4 = Mississauga.objects.all()[3]
                distance4.distance_from_user = location_4
                distance4.save()

                location5 = (43.5770557, -79.6455893)
                location_5 = round(great_circle(users_coordinates, location5).kilometers,1)
                distance5 = Mississauga.objects.all()[4]
                distance5.distance_from_user = location_5
                distance5.save()

                location6 = (43.524095, -79.6823651)
                location_6 = round(great_circle(users_coordinates, location6).kilometers,1)
                distance6 = Mississauga.objects.all()[5]
                distance6.distance_from_user = location_6
                distance6.save()

                location7 = (43.5985631, -79.6606921)
                location_7 = round(great_circle(users_coordinates, location7).kilometers,1)
                distance7 = Mississauga.objects.all()[6]
                distance7.distance_from_user = location_7
                distance7.save()

                location8 = (43.5827346, -79.7651334)
                location_8 = round(great_circle(users_coordinates, location8).kilometers,1)
                distance8 = Mississauga.objects.all()[7]
                distance8.distance_from_user = location_8
                distance8.save()

                context["qs"] = Mississauga.objects.all().order_by('distance_from_user')

                return context
            
            if location == 'Brampton':

                location1 = (43.7132335, -79.7270175)
                location_1 = round(great_circle(users_coordinates, location1).kilometers,1)
                distance1 = Brampton.objects.all()[0]
                distance1.distance_from_user = location_1
                distance1.save()

                location2 = (43.7496824, -79.7265718)
                location_2 = round(great_circle(users_coordinates, location2).kilometers,1)
                distance2 = Brampton.objects.all()[1]
                distance2.distance_from_user = location_2
                distance2.save()

                location3 = (43.6587437, -79.7498416)
                location_3 = round(great_circle(users_coordinates, location3).kilometers,1)
                distance3 = Brampton.objects.all()[2]
                distance3.distance_from_user = location_3
                distance3.save()

                location4 = (43.6335496, -79.77034)
                location_4 = round(great_circle(users_coordinates, location4).kilometers,1)
                distance4 = Brampton.objects.all()[3]
                distance4.distance_from_user = location_4
                distance4.save()

                location5 = (43.6834157, -79.7122661)
                location_5 = round(great_circle(users_coordinates, location5).kilometers,1)
                distance5 = Brampton.objects.all()[4]
                distance5.distance_from_user = location_5
                distance5.save()

                location6 = (43.658418, -79.8169362)
                location_6 = round(great_circle(users_coordinates, location6).kilometers,1)
                distance6 = Brampton.objects.all()[5]
                distance6.distance_from_user = location_6
                distance6.save()

                location7 = (43.6510185, -79.7584448)
                location_7 = round(great_circle(users_coordinates, location7).kilometers,1)
                distance7 = Brampton.objects.all()[6]
                distance7.distance_from_user = location_7
                distance7.save()

                location8 = (43.7077189, -79.7825675)
                location_8 = round(great_circle(users_coordinates, location8).kilometers,1)
                distance8 = Brampton.objects.all()[7]
                distance8.distance_from_user = location_8
                distance8.save()

                location9 = (43.6836958, -79.8154916)
                location_9 = round(great_circle(users_coordinates, location9).kilometers,1)
                distance9 = Brampton.objects.all()[8]
                distance9.distance_from_user = location_9
                distance9.save()

                location10 = (43.7855394, -79.6596981)
                location_10 = round(great_circle(users_coordinates, location10).kilometers,1)
                distance10 = Brampton.objects.all()[9]
                distance10.distance_from_user = location_10
                distance10.save()

                location11 = (43.7723278, -79.6620749)
                location_11 = round(great_circle(users_coordinates, location11).kilometers,1)
                distance11 = Brampton.objects.all()[10]
                distance11.distance_from_user = location_11
                distance11.save()

                context["qs"] = Brampton.objects.all().order_by('distance_from_user')

                return context
            
            if location == 'Ottawa':

                location1 = (45.3733998, -75.6642724)
                location_1 = round(great_circle(users_coordinates, location1).kilometers,1)
                distance1 = Ottawa.objects.all()[0]
                distance1.distance_from_user = location_1
                distance1.save()

                location2 = (45.3778586, -75.6459656)
                location_2 = round(great_circle(users_coordinates, location2).kilometers,1)
                distance2 = Ottawa.objects.all()[1]
                distance2.distance_from_user = location_2
                distance2.save()

                location3 = (45.354899, -75.6547546)
                location_3 = round(great_circle(users_coordinates, location3).kilometers,1)
                distance3 = Ottawa.objects.all()[2]
                distance3.distance_from_user = location_3
                distance3.save()

                location4 = (45.3722133, -75.6630484)
                location_4 = round(great_circle(users_coordinates, location4).kilometers,1)
                distance4 = Ottawa.objects.all()[3]
                distance4.distance_from_user = location_4
                distance4.save()

                context["qs"] = Ottawa.objects.all().order_by('distance_from_user')

                return context

class PharmacyDetailView(DetailView):
    model = Toronto

class PharmacyDetailView2(DetailView):
    model = Hamilton

class PharmacyDetailView3(DetailView):
    model = Mississauga

class PharmacyDetailView4(DetailView):
    model = Brampton

class PharmacyDetailView5(DetailView):
    model = Ottawa

class TorontoMap(DetailView):
    template_name = 'user/toronto_direction.html'
    model = Toronto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ds"] = Information.objects.all()
        return context

class HamiltonMap(DetailView):
    template_name = 'user/hamilton_direction.html'
    model = Hamilton
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ds"] = Information.objects.all()
        return context

class MississaugaMap(DetailView):
    template_name = 'user/mississauga_direction.html'
    model = Mississauga
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ds"] = Information.objects.all()
        return context

class BramptonMap(DetailView):
    template_name = 'user/brampton_direction.html'
    model = Brampton
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ds"] = Information.objects.all()
        return context

class OttawaMap(DetailView):
    template_name = 'user/ottawa_direction.html'
    model = Ottawa
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ds"] = Information.objects.all()
        return context

        