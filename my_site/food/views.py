from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import ItemForm
from .models import Item
from django.template import loader

# Create your views here.

# home page
class IndexClassView( ListView ):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_details'

def item( request ):
    return HttpResponse( "This is an item" )

# to show the details of product
# def detail( request, item_id ):
#     item = Item.objects.get( pk = item_id )
#     context = {
#         'item': item
#     }
#     return render( request, 'food/detail.html', context )

class FoodDetail( DetailView ):
    model = Item
    template_name = 'food/detail.html'

# # create new item. 
# def create_item( request ):
#     form = ItemForm( request.POST or None )
    
#     if form.is_valid():
#         form.save()
#         return redirect( 'food:index' )

#     return render( request, 'food/item-form.html', { 'form': form } )


# this is a class based view for create a new item
class CreateItem( CreateView ):
    model = Item
    fields = [ 'item_name', 'itm_desc', 'itm_price', 'item_image' ]
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)

# update or edit item
def update_item( request, id ):
    item = Item.objects.get( pk = id )
    form = ItemForm( request.POST or None, instance = item )
    
    if form.is_valid():
        form.save()
        return redirect( 'food:index' )
        
    return render( request, 'food/item-form.html', { 'form': form } )

# delete item
def delete_item( request, id ):
    item = Item.objects.get( pk = id )
    if request.method == 'POST':
        item.delete()
        return redirect( 'food:index' )
    
    return render( request, 'food/item-delete.html', { 'item': item } )
