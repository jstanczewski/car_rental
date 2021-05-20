"""car_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from car_rental import settings
from viewer.views import (
    IndexView,
    ListCars,
    CarDetailsView,
    search,
    NewContractView,
    UserView,
    ExistingContractsView,
)
from accounts.views import (
    SubmittableLoginView,
    signup,
    SubmittablePasswordChangeView,
    UpdateProfileView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("cars/", ListCars.as_view(), name="cars"),
    path("login/", SubmittableLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        SubmittablePasswordChangeView.as_view(),
        name="password_change",
    ),
    path("signup/", signup, name="signup"),
    path("cars/<int:pk>/", CarDetailsView.as_view(), name="car_details"),
    path("search/", search, name="search"),
    path("contract/<int:pk>/<int:fk>/", NewContractView.as_view(), name="new_contract"),
    path("user/<int:pk>/", UserView.as_view(), name="user_view"),
    path("user/<int:pk>/update/", UpdateProfileView.as_view(), name="user_update"),
    path(
        "user/<int:pk>/contracts/",
        ExistingContractsView.as_view(),
        name="user_contracts",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
