from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from viewer.models import Car


class IndexView(TemplateView):
    template_name = "index.html"


class ListCars(ListView):
    template_name = "cars.html"
    model = Car


class CarDetailsView(DetailView):
    template_name = 'car_details.html'
    model = Car
