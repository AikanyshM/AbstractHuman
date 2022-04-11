from django import forms
from .models import Document, Worker, Project, Membership


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            'work_experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
        

