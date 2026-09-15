# File: restaurant/urls.py
# Author: Trevor Stellmach, tstell@bu.edu (09/14/26)
# Description: Restaurant site URL file

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'main', views.main, name="main_page"), # main page path
    path(r'order', views.order, name="order_page"), # order page path
    path(r'confirmation', views.confirmation, name="confirmation_page"), # confirmation page path
]