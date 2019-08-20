# snippets/urls.py
from django.urls import path
from transaction import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('transaction/', views.TransactionView.as_view()),
    path('transaction/<int:pk>/', views.TransactionDetail.as_view()),
    path('transaction/cusomter/', views.CustomerTransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)