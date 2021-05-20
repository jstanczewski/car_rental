from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from viewer.filters import UserFilter
from viewer.forms import ContractForm
from viewer.models import Car, Contract


class IndexView(TemplateView):
    template_name = "index.html"


class ListCars(ListView):
    template_name = "cars.html"
    model = Car


class CarDetailsView(DetailView):
    template_name = 'car_details.html'
    model = Car


def search(request):
    user_list = Car.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search.html', {'filter': user_filter})


class NewContractView(LoginRequiredMixin, CreateView):
    template_name = 'contract.html'
    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        # print(request)
        return super(NewContractView, self).dispatch(request, *args, **kwargs)
