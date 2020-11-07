from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("RevolvingCredit", views.RevolvingCredit, name = "RevolvingCredit"),
    path("RevolvingCreditValue", views.RevolvingCreditValue, name = "RevolvingCreditValue"),
]