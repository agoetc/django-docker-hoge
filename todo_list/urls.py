from rest_framework import routers
from .views import TodoViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'customers', CustomerViewSet)