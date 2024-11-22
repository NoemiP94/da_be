from django.contrib import admin

from goal.forms import GoalForm
from goal.models import Goal
from goal.widgets import Base64ImageWidget

# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    form = GoalForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_base64':
            kwargs['widget'] = Base64ImageWidget
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Goal, GoalAdmin)