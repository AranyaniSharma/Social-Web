from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from . import models
from django.urls import reverse

from django.views import generic
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404





class CreateGroup(LoginRequiredMixin,generic.CreateView):  #for creating your own groups
    fields=('name','description')
    model=Group


class SingleGroup(generic.DetailView):  #it will provide details of the views
    model=Group

class ListGroups(generic.ListView):# to see the list of groups
    model=Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView): #to rdirect at the backend that join the group and
    def get_redirect_url(self,*args,**kwargs):#
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})#geting th keywoed argument by clicking


        #already member of the group
    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))  #try to go to thst group or return Http404
        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except :
            messages.warning(self.request,"Warning already a member!")

        else:
            messages.success(self.request,'You are now a member!')

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):#
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})#geting th keywoed argument by clicking


    def get(self,request,*args,**kwargs):
        try :
            membership=models.GroupMember.objects.filter(
              user=self.request.user,
              group__slug=self.kwargs.get('slug')
               ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry You are not in this group')

        else:
            membership.delete()
            messages.success(self.request,'You have left a group')
        return super().get(request,*args,**kwargs)
