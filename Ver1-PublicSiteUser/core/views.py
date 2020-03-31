from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from core.models import Product


def products(request):
    products=list(Product.objects.values())

    return JsonResponse(products, safe=False)