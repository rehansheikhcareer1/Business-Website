from django.shortcuts import render
from services.models import Service

def home(request):
    """
    Homepage view - displays featured services
    """
    # Get all active services to display on homepage
    services = Service.objects.filter(is_active=True)[:6]
    
    context = {
        'services': services,
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)

def about(request):
    """
    About page view
    """
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'about.html', context)
