from django.contrib import admin
from app.models import *
from django.utils.html import format_html

# Register your models here.
class FolderItemAdmin(admin.ModelAdmin):
    def buttons(self, obj):
        button_html = """<a class="changelink" href="/update?id=%s"  target="_blank">更新文件</a>""" % obj.id
        return format_html(button_html)

   # buttons.short_description = "操作"
    list_display = ('id','file_name','type','status','resource','explain','create_dt','update_dt','buttons')  # list
    search_fields = ('file_name',)  # list

    ordering = ('-create_dt',)
# class BtSeedDetailsAdmin(admin.ModelAdmin):
#     list_display = ('btSeed','docItem')  # list
#     search_fields = ('btSeed',)  # list
class PicItemAdmin(admin.ModelAdmin):
    list_display = ('id','main','file_name', 'type','res_header','resource','status' ,'create_dt', 'update_dt')  # list


class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('id','user','folder_item','status' ,'create_dt', 'update_dt')  # list

    def folder_item(self, obj):
        return obj.folder_item.file_name
admin.site.register(FolderItem,FolderItemAdmin)
admin.site.register(PicItem,PicItemAdmin)
admin.site.register(UserToken,UserTokenAdmin)