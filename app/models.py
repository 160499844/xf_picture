from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User
# Create your models here.
class FolderItem(models.Model):
    """文件夹目录"""

    STATUS_CHOICES = (
        (u'E', u'正常'),
        (u'F', u'无效'),
    )
    TYPE_CHOICES = (
        (u'P', u'图片'),
        (u'V', u'视频'),
    )
    file_name = models.CharField('文件名', max_length=100)
    resource = models.CharField(u'文件夹位置', max_length=100,blank=True)
    explain = models.TextField(u'说明', blank=True,null=True)
    status = models.CharField(u'状态',choices=STATUS_CHOICES, max_length=10,blank=True,default='E')
    type = models.CharField(u'媒体类型',choices=TYPE_CHOICES, max_length=10,blank=True,default='P')
    create_dt = models.DateTimeField(u'添加时间',default = timezone.now,blank=True,null= True)
    update_dt = models.DateTimeField(u'修改时间',auto_now=True,blank=True,null= True)

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = '文件夹管理'
        verbose_name_plural = verbose_name

class PicItem(models.Model):
    """文件"""
    STATUS_CHOICES = (
        (u'E', u'正常'),
        (u'F', u'无效'),
    )
    main = models.ForeignKey(FolderItem, verbose_name='目录', related_name='FolderItemFK', on_delete=models.CASCADE,
                             null=True, blank=True)
    file_name = models.CharField('文件名', max_length=100)
    type = models.CharField('格式', max_length=100,null=True)
    res_header = models.CharField('响应头', max_length=100, null=True)
    resource = models.CharField(u'文件真实路径', max_length=255,blank=True)
    file_path = models.CharField(u'文件网络路径', max_length=255,blank=True,null=True)
    img_path = models.CharField(u'视频封面', max_length=255,blank=True,null=True)
    status = models.CharField(u'状态', choices=STATUS_CHOICES, max_length=10, blank=True, default='E')
    create_dt = models.DateTimeField(u'添加时间',default = timezone.now,blank=True,null= True)
    update_dt = models.DateTimeField(u'修改时间',auto_now=True,blank=True,null= True)

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = '媒体文件管理'
        verbose_name_plural = verbose_name

class UserToken(models.Model):
    """用户访问权限管理"""
    STATUS_CHOICES = (
        (u'E', u'正常'),
        (u'F', u'无效'),
    )

    user = models.ForeignKey(User, verbose_name='用户', related_name='userTokenFK', on_delete=models.CASCADE,
                             null=True, blank=True)
    folder_item = models.ForeignKey(FolderItem, verbose_name='允许访问', related_name='folderItemFK', on_delete=models.CASCADE,
                             null=True, blank=True)
    status = models.CharField(u'状态', choices=STATUS_CHOICES, max_length=10, blank=True, default='E')
    create_dt = models.DateTimeField(u'添加时间',default = timezone.now,blank=True,null= True)
    update_dt = models.DateTimeField(u'修改时间',auto_now=True,blank=True,null= True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户访问权限管理'
        verbose_name_plural = verbose_name