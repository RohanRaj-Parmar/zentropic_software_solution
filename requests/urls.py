# requests/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CustomerRequestViewSet

router = DefaultRouter()
router.register(r'api/requests', CustomerRequestViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('submit/', views.request_submission, name='submit_request'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('', include(router.urls)),
]