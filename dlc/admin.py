from django.contrib import admin

from dlc.forms import DlcForm
from dlc.models import Dlc
from dlc.widgets import Base64ImageWidget

# Register your models here.

class DlcAdmin(admin.ModelAdmin):
    form = DlcForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_base64':
            kwargs['widget'] = Base64ImageWidget
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Dlc, DlcAdmin)   
