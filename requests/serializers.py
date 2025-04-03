# First, add 'rest_framework' to INSTALLED_APPS in settings.py
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]

# requests/serializers.py
from rest_framework import serializers
from .models import CustomerRequest

class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = ['id', 'name', 'email', 'company', 'service_type', 
                  'description', 'budget', 'timeline', 'created_at', 'status']
        read_only_fields = ['id', 'created_at']

# requests/views.py (add these to the existing views.py)
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import CustomerRequestSerializer

class CustomerRequestViewSet(viewsets.ModelViewSet):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer
    permission_classes = [IsAdminUser]  # Only admins can access
    
    def get_queryset(self):
        queryset = CustomerRequest.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
