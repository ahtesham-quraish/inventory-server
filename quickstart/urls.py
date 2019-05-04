# snippets/urls.py
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from quickstart.views import product, customers
from quickstart.views import purchase
from rest_framework import  routers

urlpatterns = [
    # path('quickstart/', views.SnippetList.as_view()),
    # path('quickstart/<int:pk>/', views.SnippetDetail.as_view()),
    # path('todo/', views.TodoList.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    # path('todo/<int:pk>/', views.TodoDetail.as_view()),
    # path('auth-jwt/', obtain_jwt_token),
    # path('auth-jwt-refresh/', refresh_jwt_token),
    # path('auth-jwt-verify/', verify_jwt_token),

    path('product/', product.ProductView.as_view()),
    path('product/<int:pk>/', product.ProductDetail.as_view()),
    path('purchase/', purchase.PurchaseView.as_view()),
    path('purchase/<int:pk>/', purchase.PurchaseDetail.as_view()),
    path('customer/', customers.CustomerView.as_view()),
    path('customer/<int:pk>/', customers.CustomerDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)