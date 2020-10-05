from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews_product', views.reviews_product, name='reviews_product'),
]