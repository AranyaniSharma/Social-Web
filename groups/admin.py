from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember

#we registered herr groupmember also and also given the cacces to group member in the admins page so that he acn delete or add members


admin.site.register(models.Group)
