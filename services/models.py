from django.db import models
from django.utils import timezone

class Service(models.Model):
    """
    Service model to store business services
    Each service has title, description, image and pricing
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.title
    
    def get_short_desc(self):
        """
        Returns short description or truncated description
        """
        if self.short_description:
            return self.short_description
        return self.description[:150] + '...' if len(self.description) > 150 else self.description
