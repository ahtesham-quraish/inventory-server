from django.urls import path
from invoicce import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('invoice/', views.InvoiceView.as_view()),
    path('invoice-by-customer/',views.InvoiceByCustomer.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

