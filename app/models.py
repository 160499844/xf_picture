from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class PictureItem(models.Model):
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