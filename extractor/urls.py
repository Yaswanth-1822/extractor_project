from django.urls import path
from .views import loan_form, extract_aadhaar

urlpatterns = [
    path('', loan_form),
    path('api/extract/', extract_aadhaar),
]