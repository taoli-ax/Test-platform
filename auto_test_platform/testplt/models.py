from django.db import models


# Create your models here.


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,verbose_name='测试项目名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '测试项目'
        verbose_name_plural = verbose_name

