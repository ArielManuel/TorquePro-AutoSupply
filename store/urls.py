from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("register-purchase/", views.register_purchase, name="register_purchase"),
    path("register-purchase/success/", views.purchase_success, name="purchase_success"),
]
