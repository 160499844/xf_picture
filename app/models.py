from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class FolderItem(models.Model):
    """相册目录"""

    STATUS_CHOICES = (
        (u'E', u'生效'),
        (u'F', u'失效'),
    )
    file_name = models.CharField('文件名', max_length=100)
    resource = models.CharField(u'文件夹位置', max_length=100,blank=True)
    explain = models.TextField(u'说明', blank=True,null=True)
    status = models.CharField(u'状态',choices=STATUS_CHOICES, max_length=10,blank=True,default='E')
    create_dt = models.DateTimeField(u'添加时间',default = timezone.now,blank=True,null= True)
    update_dt = models.DateTimeField(u'修改时间',auto_now=True,blank=True,null= True)

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = '相册目录'
        verbose_name_plural = verbose_name

class PicItem(models.Model):
    """图片"""

    main = models.ForeignKey(FolderItem, verbose_name='目录', related_name='FolderItemFK', on_delete=models.CASCADE,
                             null=True, blank=True)
    file_name = models.CharField('文件名', max_length=100)
    type = models.CharField('格式', max_length=100,null=True)
    res_header = models.CharField('响应头', max_length=100, null=True)
    resource = models.CharField(u'文件夹位置', max_length=255,blank=True)

    create_dt = models.DateTimeField(u'添加时间',default = timezone.now,blank=True,null= True)
    update_dt = models.DateTimeField(u'修改时间',auto_now=True,blank=True,null= True)

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = '图片媒体文件'
        verbose_name_plural = verbose_name