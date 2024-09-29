from django.shortcuts import render,redirect
from django.urls import path, include
from . import views
from .views import CustomPasswordResetView, admin_dashboard, custom_login, delete_supplier, edit_supplier, index, manage_suppliers, order_list_search, order_product, purchase_orders, register_supplier, select_supplier, stock_management, supplier_dashboard, update_product_quantity, user_register
from .views import index, user_register, combined_login, search, combined_login, admin_add, adminpage, edit_product, delete_product, add_to_cart, decrease_to_cart, cart, checkout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin_login/', views.combined_login, name='combined_login'),
    
    path('search/', views.search, name='search'),
    path('login/', views.combined_login, name='user_login'),
    path('user_login/', views.combined_login, name='combined_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin_add/', views.admin_add, name='admin_add'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminpageorder/', views.admin_order_view, name='adminorders'),
    path('adminordersiteam/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('userpageorder/', views.user_order_view, name='orders'),
    path('', views.index, name='index'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),

    path('reorder_level/<int:product_id>/', views.reorder_level, name='reorder_level'),

    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_to_wishlist/<int:product_id>/', views.remove_to_wishlist, name='remove_to_wishlist'),
    path('dec_from_cart/<int:product_id>/', views.decrease_to_cart, name='decrease_quantity'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('view_to_wishlist/', views.view_to_wishlist, name='view_to_wishlist'),
    path('checkout/', views.checkout_view, name='checkout'),  
    path('order_summary/', views.order_summary_view, name='order_summary'),  
    # path('profile/update/', views.profile_update, name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('profile/update/', views.profile_update, name='profile_update'),
    path('update_status/<int:order_id>/', views.update_status, name='update_status'),
    path('order_list_and_detail/', views.order_list_and_detail, name='order_list_and_detail'),
    path('orders/', order_list_search, name='order_list'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('stock_management/', stock_management, name='stock_management'),
    
    path('about.html', views.about, name='about'),
    path('order_success.html', views.success, name='success'),
    path('services.html', views.services, name='services'),
    path('ourproducts.html', views.ourproducts, name='ourproducts'),
    path('photogallery.html', views.photogallery, name='photogallery'),
    path('contact.html', views.contact, name='contact'),

    # path('purchase_cart/<int:product_id>/', purchase_cart, name='purchase_cart'),
    path('most_ordered_product/', views.index, name='most_ordered_product'),

    path('register/supplier/', register_supplier, name='register_supplier'), 
    path('supplier/login/', custom_login, name='custom_login'),
    path('purchase_orders/', purchase_orders, name='purchase_orders'),
    path('supplier/dashboard/', supplier_dashboard, name='supplier_dashboard'),
    path('order/<int:product_id>/', order_product, name='order_product'),
    path('proceed_order/', views.proceed_order, name='proceed_order'),
    path('update_product_quantity/', update_product_quantity, name='update_product_quantity'),
    path('supplier/edit/<int:product_id>/', views.supplier_edit, name='supplier_edit'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    path('manage_suppliers/', manage_suppliers, name='manage_suppliers'),
    path('edit_supplier/<int:supplier_id>/', edit_supplier, name='edit_supplier'),


    path('purchase-orders/', views.purchase_order_list, name='purchase_order_list'),

    path('restocked-products/', views.restocked_products, name='restocked_products'),
    path('delete_supplier/<int:supplier_id>/', delete_supplier, name='delete_supplier'),
    path('select_supplier/<int:order_id>/', select_supplier, name='supplier_select'),

    path('weather-dashboard/', views.weather_dashboard, name='weather_dashboard'),
    path('weather/', views.weather_view, name='weather_view'),

    path('weather-map/', views.weather_map, name='weather_map'),
    path('weather_forecast', views.weather_forecast, name='weather_forecast'),
    path('chat/', views.chat, name='chat'),
    path('recommend/', views.recommend_products, name='recommend_products'),
    path('product_visualizations/', views.product_visualizations, name='product_visualizations'),

    path('monthly_sales/',views.monthly_sales_report,name='monthly_sales'),

]
