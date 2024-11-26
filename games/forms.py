from django import forms

from games.models import VideoGame



class VideoGameForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = VideoGame
        fields = ['title',
            'year',
            'storyline',
            'gameplay',
            'engine',
            'game_mode',
            'pc_system_OS',
            'pc_system_CPU',
            'pc_system_RAM',
            'pc_graphics_card',
            'pc_graphics_memory',
            'pc_hard_drive',
            'pc_other',
            'mac_system_OS',
            'mac_system_CPU',
            'mac_system_RAM',
            'mac_graphics_card',
            'mac_graphics_memory',
            'mac_hard_drive',
            'mac_other', 'image_file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            instance.save_image_as_base64(image_file)
        if commit:
            instance.save()
        return instance