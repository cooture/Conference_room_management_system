from time import timezone

from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    sex = models.IntegerField(choices=((0, '男'), (1, '女')), default=0, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False, default='null')
    email = models.EmailField(null=False, blank=False, default='null')
    position = models.CharField(max_length=50, null=False, blank=False, default='null')
    addtime = models.DateTimeField(auto_now_add=True)
    edittime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name



class room(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, default='null')
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=False, blank=False, default='null')
    comment = models.TextField(max_length=500, default="备注为空", null=True, blank=True)
    addtime = models.DateTimeField(auto_now_add=True)
    edittime = models.DateTimeField(auto_now=True)
    manager = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "会议室"
        verbose_name_plural = verbose_name


class meeting(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    theme = models.CharField(max_length=200, null=False, blank=False, default='null')
    comment = models.TextField(max_length=1000,null=True, blank=True, default="备注为空")
    person = models.ManyToManyField(user, verbose_name="会议人员", related_name='person')
    creat_person = models.ForeignKey(user, default='null', on_delete=models.SET_DEFAULT, related_name='creat_person',
                                     null=True, blank=True, verbose_name="管理员")
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    addtime = models.DateTimeField(auto_now_add=True)
    edittime = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "会议"
        verbose_name_plural = verbose_name
        # ordering = ['starttime']




