from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)  # Campo per caricare l'immagine

    class Meta:
        model = Goal
        fields = ['name', 'requirements', 'points', 'award_type', 'game','dlc', 'image_file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            instance.save_image_as_base64(image_file)
        if commit:
            instance.save()
        return instance
