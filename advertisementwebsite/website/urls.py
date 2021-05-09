from django.urls import path
from .views import HomeView, Item, AddAdvertisement

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('item/<int:pk>', Item.as_view(), name="show_item"),
    path('addadvertisement/', AddAdvertisement.as_view(), name="add_advertisement"),
]