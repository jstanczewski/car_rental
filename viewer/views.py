from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from viewer.models import Car


class IndexView(TemplateView):
    template_name = "index.html"


class ListCars(ListView):
    template_name = "cars.html"
    model = Car
