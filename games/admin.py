from django.contrib import admin

from games.forms import VideoGameForm
from games.widgets import Base64ImageWidget
from .models import VideoGame
# Register your models here.

class VideoGameAdmin(admin.ModelAdmin):
    form = VideoGameForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            kwargs['widget'] = Base64ImageWidget
        return super().formfield_for_dbfield(db_field, **kwargs)



admin.site.register(VideoGame, VideoGameAdmin )