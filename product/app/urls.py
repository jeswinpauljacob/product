from django.urls import path

from . import views
urlpatterns = [
    path('', views.productlist.as_view(), name='product_list'),
    path('view/<int:pk>', views.productView.as_view(), name='product_view'),
    path('new', views.productCreate.as_view(), name='product_new'),
    path('edit/<int:pk>', views.productUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.productDelete.as_view(), name='product_delete'),

]