from django.forms.widgets import ClearableFileInput

class Base64ImageWidget(ClearableFileInput):
    template_name = 'base64_image_widget.html'

    def format_value(self, value):
        return None

