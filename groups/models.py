from django.conf import settings
from django.db import models
from django.utils.text import slugify#remove characters
import misaka #rendering markdown we installed it
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register=template.Library

# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True) #SlugField in Django is like a CharField, where you can specify max_length attribute also. If max_length is not specified, Django will use a default length of 50. I
    description=models.TextField(blank=True,default='')
    description_html=models.TextField(editable=False,default='',blank=True)
    members=models.ManyToManyField(User,through='GroupMember')#all the member to this particular group

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):#to saVE A GROUP
        self.slug=slugify(self.name)  #removecharacters hyphens and donlower removecharactershyphensanddo lower cases
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})
    class Meta:
        ordering =['name']


class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)


    def __str__(self):
        return self.username

    class Meta:
        unique_together=('group','user')
