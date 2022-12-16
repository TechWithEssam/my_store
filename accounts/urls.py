from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("my-account/", views.account_sales_view, name="my_account"),
    path("create-account/", views.create_account_view, name="create_account"),
    path("update-account/", views.update_information_your_account, name="update_account"),
    path("account/<slug:url>/", views.detail_account_buyer_view, name="detail_buyer"),
    path("action/follow-unfollow/", views.action_follow_unfollow_view, name="follow_unfollow"),
    path("delete/<int:pk>/", views.delete_my_account_view, name="delete_account"),
    path('update-product/<str:slug>/', views.update_my_product_view, name="update_product"),
    path('delete-product/<str:slug>/', views.delete_product_view, name="delete_product"),
    path('my-all-orders/', views.my_orders_view, name="my_orders_and_sales"),
    path('my-all-orders/<slug:done>/', views.my_orders_view, name="my_orders_and_sales_done"),
    path("detail-orders/<int:pk>/", views.detail_order_view, name="detail_order"),
]