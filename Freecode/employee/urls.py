from django.urls import path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'', )

urlpatterns = [
    path('', views.EmployeeSet.as_view()),
]


