from re import template
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.

def index( request ):
    item_details = Item.objects.all()
    context = {
        'item_details': item_details
    }
    return render( request, 'food/index.html', context )

def item( request ):
    return HttpResponse( "This is an item" )

def detail( request, item_id ):
    item = Item.objects.get( pk = item_id )
    context = {
        'item': item
    }
    return render( request, 'food/detail.html', context )

# def head( request ):
#     return HttpResponse( '<h1>This is the heading</h1>' )
