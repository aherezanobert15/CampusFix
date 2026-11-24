from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from accounts.models import User
from .forms import IncidentForm
from .models import Incident

@login_required
def report_incident(request):

    allowed_roles = [
        User.Role.STUDENT,
        User.Role.LECTURER,
    ]

    # Allow students and lecturers to report incidents.
    # Superusers retain administrative access.
    if not request.user.is_superuser:
        if request.user.role not in allowed_roles:
            raise PermissionDenied(
                "You are not authorized to report incidents."
            )

    if request.method == 'POST':

        form = IncidentForm(request.POST)

        if form.is_valid():

            incident = form.save(commit=False)

            incident.reporter = request.user

            incident.save()

            messages.success(
                request,
                'Your incident has been reported successfully!'
            )

            return redirect('report_incident')

    else:

        form = IncidentForm()

    context = {
        'form': form
    }

    return render(
        request,
        'incidents/report_incident.html',
        context
    )

@login_required
def incident_dashboard(request):

    user = request.user

    if user.is_superuser or user.role in [
        User.Role.IT_ADMIN,
        User.Role.SYSTEM_ADMIN,
    ]:

        incidents = Incident.objects.all()

    elif user.role == User.Role.TECHNICIAN:

        incidents = Incident.objects.filter(
            assigned_technician=user
        )

    elif user.role in [
        User.Role.STUDENT,
        User.Role.LECTURER,
    ]:

        incidents = Incident.objects.filter(
            reporter=user
        )

    else:

        raise PermissionDenied(
            "You are not authorized to access this dashboard."
        )

    incidents = incidents.select_related(
        'reporter',
        'assigned_technician'
    ).order_by('-created_at')

    context = {
        'incidents': incidents,
    }

    return render(
        request,
        'incidents/dashboard.html',
        context
    )
