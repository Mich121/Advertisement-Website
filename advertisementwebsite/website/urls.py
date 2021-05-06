from django.urls import path
from .views import HomeView, Item

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('item/<int:pk>/', Item.as_view(), name="item"),
]