from django.urls import path
from shop import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail-product/', views.detail_product, name='detail')
]
