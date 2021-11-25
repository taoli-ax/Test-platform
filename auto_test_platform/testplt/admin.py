from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)
admin.site.site_title = '自动化测试平台'
admin.site.site_header = '自动化测试平台'
