from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path('my-profile/', views.my_profile_view, name="my_profile"),
    path("register/", views.register_user_view, name="register"),
    path('login/', views.login_user_view, name="login"),
    path('logout/', views.logout_user_view, name="logout"),
    path("subscribe/", views.user_news_subscribe_view, name="subscribe"),
    path("change-password/", views.change_password_view, name="change_password"),
    path("update-info/", views.update_information_user, name="ypdate_info"),
]