from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path("activate/<email_token>/", views.activate_email, name="activate"),
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<uid>/", views.add_to_cart, name="add_to_cart"),
    path("delete-cart/<uid>/", views.delete_cart, name="delete_cart"),

]
