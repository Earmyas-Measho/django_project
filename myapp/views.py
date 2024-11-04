# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Item, Contract

def home(request):
    return HttpResponse("Welcome to the Home Page")

def member_list(request):
    members = Member.objects.all()  # Retrieve all members from the database
    return render(request, 'myapp/member_list.html', {'members': members})

def item_list(request):
    items = Item.objects.all()  # Retrieve all items from the database
    return render(request, 'myapp/item_list.html', {'items': items})

def contract_list(request):
    contracts = Contract.objects.all()  # Retrieve all contracts from the database
    return render(request, 'myapp/contract_list.html', {'contracts': contracts})
