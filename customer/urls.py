# snippets/urls.py
from django.urls import path
from customer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('customer/', views.CustomerView.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)