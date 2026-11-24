from django import forms
from .models import Incident
from django.contrib.auth import get_user_model

User = get_user_model()


class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident

        fields = [
            'title',
            'description',
            'category',
            'priority',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short title for your problem'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Explain the problem in detail'
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
        }



class AssignTechnicianForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ['assigned_technician']

        widgets = {
            'assigned_technician': forms.Select(
                attrs={'class': 'form-select'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['assigned_technician'].queryset = (
            User.objects.filter(role='TECHNICIAN')
            .order_by('username')
        )

        self.fields['assigned_technician'].required = True


class UpdateIncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ['status', 'resolution_notes']

        widgets = {
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'resolution_notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Explain the work performed...'
                }
            )
        }

    def __init__(self, *args, user=None, **kwargs):

        super().__init__(*args, **kwargs)

        # Technicians can only move their assigned
        # incidents forward in the workflow.
        if user and user.role == 'TECHNICIAN':

            self.fields['status'].choices = [
                ('IN_PROGRESS', 'In Progress'),
                ('RESOLVED', 'Resolved')
            ]
