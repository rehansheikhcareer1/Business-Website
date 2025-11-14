from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    """
    Display all active services
    """
    services = Service.objects.filter(is_active=True)
    
    context = {
        'services': services,
        'page_title': 'Our Services'
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, pk):
    """
    Display individual service details
    """
    service = get_object_or_404(Service, pk=pk, is_active=True)
    
    # Get related services (same category or recent)
    related_services = Service.objects.filter(is_active=True).exclude(pk=pk)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
        'page_title': service.title
    }
    return render(request, 'services/service_detail.html', context)
