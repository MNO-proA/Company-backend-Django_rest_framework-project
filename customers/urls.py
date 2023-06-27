from django.urls import path
from customers import views


urlpatterns = [
    path('', views.customers, name='customers'),
    path('<int:id>', views.customer, name='customer')
]