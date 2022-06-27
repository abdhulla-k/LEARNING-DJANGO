from django.urls import path
from . import views


urlpatterns = [
    path( '', views.index, name = 'index' ),
    path( 'item/', views.item, name = 'item' ),
    # path( 'head/', views.head, name = 'head' )
]