from django.urls import path
from . import views


app_name = 'food'   # name spacing. add this name to urls of this app
urlpatterns = [
    path( '', views.IndexClassView.as_view(), name = 'index' ),
    path( '<int:pk>/', views.FoodDetail.as_view(), name = 'detail' ),
    path( 'item/', views.item, name = 'item' ),
    # add new_item
    path( 'add/', views.CreateItem.as_view(), name = 'create_item' ),
    # edit item
    path( 'update/<int:id>/', views.update_item, name = 'update_item' ),
    # delete an item
    path( 'delete/<int:id>/', views.delete_item, name = 'delete_item' )
]