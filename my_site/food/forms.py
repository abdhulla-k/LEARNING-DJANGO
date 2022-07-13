from .models import Item
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [ 'item_name', 'itm_desc', 'itm_price', 'item_image' ]