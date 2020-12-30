from django.urls import path
from rest_framework.authtoken import views

from ecommerce.resources.manage_orders import ManageOrders
from ecommerce.resources.registration import Registration

app_name = 'ecommerce'
urlpatterns = [
    path('v1/login', views.obtain_auth_token),
    path('v1/signup', Registration.as_view(), name="signup"),
    path('v1/orders', ManageOrders.as_view(), name="orders"),
]
