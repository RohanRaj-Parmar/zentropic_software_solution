# requests/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomerRequestForm
from .models import CustomerRequest
from rest_framework import viewsets
from .models import CustomerRequest
from .serializers import CustomerRequestSerializer

class CustomerRequestViewSet(viewsets.ModelViewSet):
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializer

def home_view(request):
    form = CustomerRequestForm()
    return render(request, 'requests/home.html', {'form': form})

def request_submission(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerRequestForm()
    return render(request, 'requests/home.html', {'form': form})

class SuccessView(TemplateView):
    template_name = 'requests/success.html'