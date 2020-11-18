from django.urls import path,include
from rest_framework import routers
from . import views
# from rest_framework.authtoken import views 

# router = routers.DefaultRouter()
# router.register(r'', )

urlpatterns = [
    path('product/<int:id>', views.ProductView.as_view()),
    path('',views.CategoryView.as_view()),
    path('addtocart/<int:id>',views.addtocart, name="addtocart"),
    path('removecart/<int:id>',views.remove_from_cart, name='remove_from_cart'),
    path('rtemove/<int:id>',views.remove_single_item_from_cart, name='remove_single_item_from_cart')
    # path('login',include(rest_framework.urls))
    # path('add-to-cart/<int:id>',views.AddToCart.as_view())
]


