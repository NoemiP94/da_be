from django import forms

from characters.models import Character



class CharacterForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Character
        fields = ['name', 'charcClass', 'specialisation', 'where', 'title', 'affiliation',
                  'gender', 'race', 'romanceable', 'game', 'description', 'image_file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            instance.save_image_as_base64(image_file)
        if commit:
            instance.save()
        return instance