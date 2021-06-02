"""vaccine_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as user_views
from rides import views as rides_views
from rides.views import UberView
from user.views import InformationView, PharmacyDetailView, PharmacyDetailView2, PharmacyDetailView3, PharmacyDetailView4, PharmacyDetailView5, TorontoMap, HamiltonMap, MississaugaMap, BramptonMap, OttawaMap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('user-info/', user_views.get_info, name='user-info'),
    path('listpharmacy/', InformationView.as_view(), name='listpharmacy'),
    path('listpharmacy-detail/toronto/<int:pk>/', PharmacyDetailView.as_view(), name='listpharmacy-detail'),
    path('listpharmacy-detail/hamilton/<int:pk>/', PharmacyDetailView2.as_view(), name='listpharmacy-detail2'),
    path('listpharmacy-detail/mississauga/<int:pk>/', PharmacyDetailView3.as_view(), name='listpharmacy-detail3'),
    path('listpharmacy-detail/brampton/<int:pk>/', PharmacyDetailView4.as_view(), name='listpharmacy-detail4'),
    path('listpharmacy-detail/ottawa/<int:pk>/', PharmacyDetailView5.as_view(), name='listpharmacy-detail5'),
    path('directions/toronto/<int:pk>/', TorontoMap.as_view(), name='direction1'),
    path('directions/hamilton/<int:pk>/', HamiltonMap.as_view(), name='direction2'),
    path('directions/mississauga/<int:pk>/', MississaugaMap.as_view(), name='direction3'),
    path('directions/brampton/<int:pk>/', BramptonMap.as_view(), name='direction4'),
    path('directions/ottawa/<int:pk>/', OttawaMap.as_view(), name='direction5'),
    path('uber-main/', UberView.as_view(), name='uber-main'),
    path('ride-main/', rides_views.get_ride_info, name='ride-main'),
]
