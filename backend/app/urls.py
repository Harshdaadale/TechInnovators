from django.urls import path
from . import views

urlpatterns = [
    path("retailer-signup/", views.retailer_signup, name="retailer-signup"),
    path("aboutus/", views.aboutus, name="aboutus"),
]
