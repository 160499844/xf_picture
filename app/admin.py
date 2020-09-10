from django.contrib import admin
from app.models import *
# Register your models here.
class PicAdmin(admin.ModelAdmin):
    # def buttons(self, obj):
    #     button_html = """<a class="changelink" href="/downloadBt?id=%s"  target="_blank">下载种子</a>""" % obj.id
    #     return format_html(button_html)

   # buttons.short_description = "操作"
    list_display = ('file_name','resource','explain','status','create_dt','update_dt')  # list
    search_fields = ('file_name',)  # list

    ordering = ('-create_dt',)
# class BtSeedDetailsAdmin(admin.ModelAdmin):
#     list_display = ('btSeed','docItem')  # list
#     search_fields = ('btSeed',)  # list


admin.site.register(PictureItem,PicAdmin)