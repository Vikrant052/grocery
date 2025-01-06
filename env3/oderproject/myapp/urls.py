

from django.urls import path
from .views import OrderAPIList, OrderAPIDetail

urlpatterns = [
    path('orders/', OrderAPIList.as_view(), name='order-list'),  
    path('orders/<int:id>/', OrderAPIDetail.as_view(), name='order-detail'),  
]
