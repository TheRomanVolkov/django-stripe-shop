from django.urls import path
from items.views import ItemDetailView, ItemListView, home
from items.views_api import CreateCheckoutSessionAPI, ItemDetailAPI

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('api/buy/<int:id>/', CreateCheckoutSessionAPI.as_view(), name='api_create_checkout_session'),
    path('api/item/<int:id>/', ItemDetailAPI.as_view(), name='api_item_detail'),
]
