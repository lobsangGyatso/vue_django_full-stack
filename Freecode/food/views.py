from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer, ProductSerializer,orderItemSerializer,OrderSerializer
from .models import Category, orderItem, Product,Order
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth import login as django_login,logout as django_logout
# Create your views here.
class  ProductView(APIView):
    
    def get(self, request, id):
        obj=Category.objects.get(id=id)
        product = Product.objects.filter(cat=obj)
        serializers = ProductSerializer(product,many = True)
        return Response(serializers.data)

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status  = 200)


class CategoryView(APIView):
    def get(self,request):
        cat=Category.objects.all()
        serializers = CategorySerializer(cat, many = True)
        return Response(serializers.data)
        

# class AddToCart(APIView):
    
#     def post(self, request, id):
#         print(id)
def addtocart(request, id):
    # first get the object 
  u=User.objects.get(id=2)
  item = get_object_or_404(Product, pk=id)
  order_item, created = orderItem.objects.get_or_create(
    user = u,
    product = item
  )
  order_qs = Order.objects.filter(user=u)
  print("order_qs",order_qs)
  if order_qs.exists():
    order = order_qs[0]
    print("order",order)
    print("lobsang gyatso",order.product.filter(product_id=item.id))
    if order.product.filter(product_id=item.id).exists():
        order_item.quantity += 1
        order_item.save()
    else:
        order.product.add(order_item)
  else:
    order = Order.objects.create(
        user=u
        )
    order.product.add(order_item)



def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.product.filter(product_id=item.id).exists():
            order_item = orderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
        else:
            pass
    else:
        pass


# @login_required
def remove_single_item_from_cart(request, id):
    item = get_object_or_404(Item, pk=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.product.filter(product_id=item.id).exists():
            order_item = orderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            pass
        else:
           pass
    else:
       pass




# class LoginView(APIView):
#     def post(self,request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         user = serializer.validate_data["user"]
#         django_login(request,user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token":token.key},status=200)

# class LogoutView(APIView):
#     authentication_classes  = (TokenAuthentication, )
#     def post(self, request):
#         django_logout(request)