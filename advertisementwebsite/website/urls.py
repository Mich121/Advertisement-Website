from django.urls import path
from .views import HomeView, Item, AddAdvertisement, DeleteAdvert, UpdateAdvert

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('item/<int:pk>', Item.as_view(), name="show_item"),
    path('addadvertisement/', AddAdvertisement.as_view(), name="add_advertisement"),
    path('deleteadvert/<int:pk>/', DeleteAdvert.as_view(), name="delete_advert"),
    path('updateadvert/<int:pk>/', UpdateAdvert.as_view(), name="update_advert"),
]