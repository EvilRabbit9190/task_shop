from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "get_image", "cost", "raiting")
    list_filter = ("cost", "raiting")

    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width="100" height="110"')
        else:
            return mark_safe(f'<img src="" alt="" width="100" height="110"')


admin.site.site_header = "Административная панель Shop Disney"
admin.site.index_title = "Модели"
admin.site.register(Good, GoodAdmin)