from django import forms as f

from .models import Birthday


class BirthdayForm(f.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': f.DateInput(attrs={'type': 'date'})
        }
