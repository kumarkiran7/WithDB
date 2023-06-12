from django.urls import path
from .views import *

urlpatterns = [
    path ('employee_details/',employee_details),
    path ('employee_hist/',employee_hist),
]