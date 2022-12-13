from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='productsbycat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proDetail')

]
