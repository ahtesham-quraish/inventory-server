# snippets/urls.py
from django.urls import path
from type import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('type/', views.TypeView.as_view()),
    path('type/<int:pk>/', views.TypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)