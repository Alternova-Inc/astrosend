from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string

from .models import AllowedDomain, AuthCode


def login_page(request):
    """Render the login page with email input"""
    return render(request, 'auth_app/login.html')


@csrf_protect
@require_http_methods(["POST"])
def verify_email(request):
    """Check if email is allowed and send verification code"""
    email = request.POST.get('email', '').strip().lower()
    
    if not email:
        return HttpResponse(
            render_to_string('auth_app/email_form.html', {
                'error': 'Email is required'
            }),
            status=400
        )
    
    # Check if the email domain is allowed
    if not AllowedDomain.is_email_allowed(email):
        return HttpResponse(
            render_to_string('auth_app/email_form.html', {
                'error': 'This email domain is not allowed',
                'email': email
            }),
            status=400
        )
    
    # Generate authentication code
    auth_code = AuthCode.generate_code(email)
    
    # Send the code via email
    email_subject = "Your AstroSend Verification Code"
    email_body = f"Your verification code is: {auth_code.code}\n\nThis code will expire in 10 minutes."
    
    try:
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        
        # Return the code verification form
        return HttpResponse(
            render_to_string('auth_app/code_form.html', {
                'email': email
            })
        )
        
    except Exception as e:
        # Log the error in a production environment
        print(f"Email sending error: {str(e)}")
        
        return HttpResponse(
            render_to_string('auth_app/email_form.html', {
                'error': 'Failed to send verification code. Please try again.',
                'email': email
            }),
            status=500
        )


@csrf_protect
@require_http_methods(["POST"])
def verify_code(request):
    """Verify the authentication code"""
    email = request.POST.get('email', '').strip().lower()
    code = request.POST.get('code', '').strip()
    
    if not email or not code:
        return HttpResponse(
            render_to_string('auth_app/code_form.html', {
                'error': 'Email and code are required',
                'email': email
            }),
            status=400
        )
    
    # Get the most recent unused code for this email
    try:
        auth_code = AuthCode.objects.filter(
            email=email,
            used=False
        ).order_by('-created_at').first()
        
        if not auth_code or not auth_code.is_valid():
            return HttpResponse(
                render_to_string('auth_app/code_form.html', {
                    'error': 'Invalid or expired code',
                    'email': email
                }),
                status=400
            )
        
        if auth_code.code != code:
            return HttpResponse(
                render_to_string('auth_app/code_form.html', {
                    'error': 'Incorrect code',
                    'email': email
                }),
                status=400
            )
        
        # Mark the code as used
        auth_code.used = True
        auth_code.save()
        
        # Authentication successful - redirect to the main application
        # In a real application, you might set a session or token here
        # but as per requirements, we don't want to maintain sessions
        
        # For now, just redirect to a success page
        return HttpResponse(
            render_to_string('auth_app/success.html', {
                'email': email
            })
        )
        
    except Exception as e:
        # Log the error in a production environment
        print(f"Code verification error: {str(e)}")
        
        return HttpResponse(
            render_to_string('auth_app/code_form.html', {
                'error': 'An error occurred. Please try again.',
                'email': email
            }),
            status=500
        )
