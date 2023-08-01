from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name= 'dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.allproducts, name= 'allproduct' ),
    path('products/sopndetergent', views.soapNdetergent, name='soapndetergent'),
    path('expiredprod/', views.expiredproducts, name= 'expired-product'),
]