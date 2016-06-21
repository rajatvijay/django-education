from django.forms.models import inlineformset_factory
from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course, Module, extra=2, can_delete=True,
                                      fields=['title', 'description'])
