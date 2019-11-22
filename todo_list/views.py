from rest_framework import viewsets
from .models import Todo, Customer
from .serializers import TodoSerializer, CustomerSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
