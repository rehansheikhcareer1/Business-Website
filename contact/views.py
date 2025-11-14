from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    """
    Handle contact form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_msg = form.save()
            
            # Send email notification to admin
            try:
                subject = f"New Contact Form: {contact_msg.subject}"
                message = f"""
                New contact form submission:
                
                Name: {contact_msg.name}
                Email: {contact_msg.email}
                Phone: {contact_msg.phone}
                Subject: {contact_msg.subject}
                
                Message:
                {contact_msg.message}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            except Exception as e:
                # Log error but don't break the flow
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact Us'
    }
    return render(request, 'contact/contact.html', context)
