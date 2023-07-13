from django.urls import path
from product import views

urlpatterns = [
    path("<slug>/", views.view_product,  name="view_product"),
]
