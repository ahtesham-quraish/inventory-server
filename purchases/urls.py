# snippets/urls.py
from django.urls import path
from purchases import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('purchase/', views.PurchaseView.as_view()),
    path('purchase/<int:pk>/', views.PurchaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)