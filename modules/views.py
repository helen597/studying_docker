from rest_framework import viewsets
from modules.paginators import MyPagination
from modules.serializers import ModuleSerializer
from modules.models import Module


# Create your views here.
class ModuleViewSet(viewsets.ModelViewSet):
    """Educational module viewset controller"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = MyPagination

    def perform_create(self, serializer):
        """Module creation function"""
        module = serializer.save()
        module.owner = self.request.user
        module.save()
