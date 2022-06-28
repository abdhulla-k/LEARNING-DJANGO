from django.urls import path
from . import views


app_name = 'food'   # name spacing. add this name to urls of this app
urlpatterns = [
    path( '', views.index, name = 'index' ),
    path( '<int:item_id>/', views.detail, name = 'detail' ),
    path( 'item/', views.item, name = 'item' ),
    # path( 'head/', views.head, name = 'head' )
]