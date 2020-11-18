from rest_framework import serializers
from django.contrib.auth.models import  User
# from rest-framework import exceptions
from .models import Order, orderItem,Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # cat=CategorySerializer()
    class Meta:
        model = Product
        fields =  (
            'id',
            'productname',
            'cat',
            'price',
            'picture'
        )

class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()


#     def validate(self,data):
#         username = data.get("username","")
#         password = data.get("password","")

#         if username and password:
#             user = authenticate(username=username,password=password)
#             if user:
#                 if user.is_active:
#                     data["user"] = user
#                 else:
#                     msg ="user is deactive"
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = "unable to login"
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = "must provide the credintial"
#             raise exceptions.ValidationError(msg)
#         return data