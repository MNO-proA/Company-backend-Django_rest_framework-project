from django.shortcuts import render
from customers.models import Customer
from customers.serializers import CustomerSerializer
from django.http import JsonResponse

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers':serializer.data})

def customer(request, id):
    data = Customer.objects.get(pk=id)
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer':serializer.data})