from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from .forms import *
from authentication.repo import ProfileRepo
from dashboard.views import getContext as DashboardContext

TEMPLATE_ROOT='material/'




def getContext(request):
    context=DashboardContext(request)
    return context

class BasicViews(View):
    def home(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)
    def features(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'features.html',context)

class ProfileViews(View):
    def profile(self,request,profile_id=0,*args,**kwargs):
        if profile_id==0:
            selected_profile=ProfileRepo(user=request.user).me
        else:
            selected_profile=ProfileRepo(user=request.user).get(profile_id=profile_id)
        context=getContext(request)
        context['body_class']='profile-page'
        context['selected_profile']=selected_profile
        return render(request,TEMPLATE_ROOT+'profile.html',context)

class ExampleViews(View):
    def all_components(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/all_components.html',context)
    def sections(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/sections.html',context)




# Create your views here.