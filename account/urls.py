# snippets/urls.py
from django.urls import path
from account import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('bank/', views.BankView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)