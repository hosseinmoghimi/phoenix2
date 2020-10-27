from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
from .repo import *
from .serializers import *
from .forms import *
import json
from .utils import AdminUtility
TEMPLATE_ROOT='projectmanager/'
def getContext(request):
    user=request.user
    context=DashboardContext(request)
    context['admin_utility']=AdminUtility()
    return context

class BasicViews(View):
    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        projects=ProjectRepo(user=user).list_roots()
        context['projects']=projects
        contractors=ContractorRepo(user=user).list()
        organiazationunits=OrganiazationUnitRepo(user=user).list_roots()
        context['organiazationunits']=organiazationunits
        context['contractors']=contractors
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form']=AddProjectForm()
        if user.has_perm(APP_NAME+'.add_contracotr'):
            context['add_contracotr_form']=AddContractorForm()
        projects_s=json.dumps(ProjectSerializer(projects,many=True).data)
        context['projects_s']=projects_s
        contractors_s=json.dumps(ContractorSerializer(contractors,many=True).data)
        context['contractors_s']=contractors_s
        return render(request,TEMPLATE_ROOT+'index.html',context)

class ApiViews(View):
    def add_project(self,request):
        user=request.user
        if request.method=='POST':
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                title=add_project_form.cleaned_data['title']
                parent_id=add_project_form.cleaned_data['parent_id']
                project=ProjectRepo(user=user).add(title=title,parent_id=parent_id)
                if project is not None:
                    project_s=ProjectSerializer(project).data
                    return JsonResponse(project_s)
    def add_contractor(self,request):
        user=request.user
        if request.method=='POST':
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                title=add_project_form.cleaned_data['title']
                contractor=ContractorRepo(user=user).add(title=title)
                if contractor is not None:
                    contractor_s=ContractorSerializer(contractor).data
                    return JsonResponse(contractor_s)
class PageViews(View):
    def project(self,request,pk,*args, **kwargs):
        project_id=pk
        user=request.user
        context=getContext(request)
        project=ProjectRepo(user=user).project(project_id=project_id)
        context['project']=project
        context['page']=project
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form']=AddProjectForm()
        return render(request,TEMPLATE_ROOT+'project.html',context)
    def event(self,request,pk,*args, **kwargs):
        event_id=pk
        user=request.user
        context=getContext(request)
        event=EventRepo(user=user).event(event_id=event_id)
        context['event']=event
        context['page']=event
        return render(request,TEMPLATE_ROOT+'event.html',context)
    def organiazationunit(self,request,pk,*args, **kwargs):
        organiazationunit_id=pk
        user=request.user
        context=getContext(request)
        organiazationunit=OrganiazationUnitRepo(user=user).organiazationunit(organiazationunit_id=organiazationunit_id)
        context['organiazationunit']=organiazationunit
        context['page']=organiazationunit
        return render(request,TEMPLATE_ROOT+'event.html',context)
    def contractor(self,request,pk,*args, **kwargs):
        contractor_id=pk
        user=request.user
        context=getContext(request)
        contractor=ContractorRepo(user=user).contractor(contractor_id=contractor_id)
        context['contractor']=contractor
        context['page']=contractor
        return render(request,TEMPLATE_ROOT+'contractor.html',context)


