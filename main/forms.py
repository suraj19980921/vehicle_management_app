from django import forms
from django.forms.widgets import HiddenInput
from main import models

class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = models.Vehicle
        fields = '__all__'
        widgets = {
                    'name' : forms.TextInput(attrs={'class':'form-control'}),
                    'camera1' : forms.FileInput(attrs={'class':'form-control'}),
                    'camera2' : forms.FileInput(attrs={'class':'form-control'}),
                    'speed' : forms.NumberInput(attrs={'class':'form-control'}),
                    'average_speed': forms.NumberInput(attrs={'class':'form-control'}),
                    'temperature': forms.NumberInput(attrs={'class':'form-control'}),
                    'fuel_level': forms.NumberInput(attrs={'class':'form-control'}),
                    'engine_status': forms.TextInput(attrs={'class':'form-control'}),
                    
        }

