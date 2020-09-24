from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'creation', 'v_id')
    ordering = ('creation', 'title')
    prepopulated_fields = {'slug': ('title',)}
