from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    """Main dashboard view that redirects to send view"""
    return render(request, 'dashboard/send.html')


@login_required
def send_secret(request):
    """View for sending new secrets"""
    return render(request, 'dashboard/send.html')


@login_required
def history(request):
    """View for viewing secret history"""
    return render(request, 'dashboard/history.html')
