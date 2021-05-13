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
from django.contrib import admin
from django.urls import path
from viewer.views import IndexView, ListCars, CarDetailsView
from accounts.views import SubmittableLoginView, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cars/', ListCars.as_view(), name='cars'),
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('cars/<int:pk>/', CarDetailsView.as_view(), name='car_details')
]
