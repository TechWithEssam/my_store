from . import views
from django.urls import path


app_name = "store"
urlpatterns = [
    path('', views.home_and_filter_product_view, name="home"),
    path('detail/<str:slug>/', views.detial_product_view, name="detail"),
    path('category/<slug:category>/', views.home_and_filter_product_view, name="filter_category"),
    path('category/<slug:category>/<slug:brand>/', views.home_and_filter_product_view, name="filter_brand"),
    path('filter-price/<slug:data>/',views.home_and_filter_product_view, name="filter_price"), 
    path('add-to-cart/', views.add_to_cart_view, name="add_to_cart"),
    path('minus-from-cart/', views.minus_product_form_cart_view, name="minus_from_cart"),
    path('cart/', views.cart_user_view, name="cart"),
    path("empty/", views.remove_product_from_cart, name="empty"),
    path("check-out/", views.order_placed_view, name="shopping"),
    path('my-orders/', views.your_order_view, name="my_order"),
    path("add-category/", views.add_new_category_view, name="add_category"),
    path("add-brand/", views.add_brand_view, name="add_brand"),
    path("add-new-product/", views.add_new_product_by_buyer_view, name="new_product"),
    path('handed/', views.handed_products_shopping, name="handed_product"),
    path('delete-order/<int:pk>/', views.delete_product_form_orders_view, name="delete_order"),
    path('store/empty-orders/', views.empty_orders_be_done_view, name="empty_orders")
]
