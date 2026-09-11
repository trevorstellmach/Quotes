# File: quotes/urls.py
# Author: Trevor Stellmach, tstell@bu.edu (09/08/26)
# Description: Quotes site URL file

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.quote, name="quote_page") # quote page path

]