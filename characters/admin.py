from django.contrib import admin

from characters.forms import CharacterForm
from characters.widgets import Base64ImageWidget
from .models import Character

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_base64':
            kwargs['widget'] = Base64ImageWidget
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Character, CharacterAdmin)
