from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from accounts.models import Profile
from viewer.filters import UserFilter
from viewer.forms import ContractForm
from viewer.models import Car, Contract


class IndexView(TemplateView):
    template_name = "index.html"


class ListCars(ListView):
    template_name = "cars.html"
    model = Car


class CarDetailsView(DetailView):
    template_name = "car_details.html"
    model = Car


class UserView(DetailView):
    template_name = "user_profile.html"
    model = Profile


class ExistingContractsView(ListView):
    template_name = "user_contracts.html"
    model = Contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract_list = self.get_queryset()
        value_dict = {}
        for contract in contract_list:
            interval = contract.date_to - contract.date_from
            value_dict[contract.id] = (int(contract.car_id.price) * interval.days)
        context['value_dict'] = value_dict
        return context


def search(request):
    user_list = Car.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, "search.html", {"filter": user_filter})


class NewContractView(LoginRequiredMixin, CreateView):
    template_name = "contract.html"
    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        self.form_class.base_fields["car_id"].initial = str(request).split("/")[2]
        self.form_class.base_fields["profile_id"].initial = str(request).split("/")[3]
        return super(NewContractView, self).dispatch(request, *args, **kwargs)
