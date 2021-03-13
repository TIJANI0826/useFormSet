# forms.py
from django.forms import modelformset_factory
from django.views.generic import ListView,TemplateView
from .models import Bird

# # A regular form, not a formset
# class BirdForm(ModelForm):
#     class Meta:
#       model = Bird
#       fields = [common_name, scientific_name]
      
BirdFormSet = modelformset_factory(
    Bird, fields=("common_name", "scientific_name"), extra=1
)
