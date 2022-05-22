from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{}" width="{}">', obj.image.url, 200)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]