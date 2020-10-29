from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
from .repo import *
from .serializers import *
from .forms import *
from dashboard.forms import AddDocumentForm,AddTagForm,AddLinkForm
import json
from dashboard.serializers import TagSerializer,DocumentSerializer,LinkSerializer
from .utils import AdminUtility
TEMPLATE_ROOT='projectmanager/'
def getContext(request):
    user=request.user
    context=DashboardContext(request)
    context['admin_utility']=AdminUtility()
    context['search_form']=SearchForm()
    return context

class BasicViews(View):
    def search(self,request,*args, **kwargs):
        if request.method=='POST':
            search_form=SearchForm(request.POST)
            if search_form.is_valid():
                search_for=search_form.cleaned_data['search_for']
                context=getContext(request)
                context['search_for']=search_for
                context['pages']=ManagerPageRepo(user=request.user).search(search_for=search_for)
                return render(request,TEMPLATE_ROOT+'search.html',context)

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

class PageViews(View):
    def getManagerPageContext(self,request,page,*args, **kwargs):
        context=getContext(request)
        context['add_tag_form']=AddTagForm()
        context['add_link_form']=AddLinkForm()
        context['add_document_form']=AddDocumentForm()
        context['tags_s']=json.dumps(TagSerializer(page.tags.all(),many=True).data)
        context['links_s']=json.dumps(LinkSerializer(page.links.all(),many=True).data)
        context['documents_s']=json.dumps(DocumentSerializer(page.documents.all(),many=True).data)
        return context
    def project(self,request,pk,*args, **kwargs):
        project_id=pk
        user=request.user
        project=ProjectRepo(user=user).project(project_id=project_id)
        context=self.getManagerPageContext(request=request,page=project)
        context['project']=project
        context['page']=project
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form']=AddProjectForm()
        return render(request,TEMPLATE_ROOT+'project.html',context)
    def event(self,request,pk,*args, **kwargs):
        event_id=pk
        user=request.user
        context=self.getManagerPageContext(request)
        event=EventRepo(user=user).event(event_id=event_id)
        context['event']=event
        context['page']=event
        return render(request,TEMPLATE_ROOT+'event.html',context)
    def organiazationunit(self,request,pk,*args, **kwargs):
        organiazationunit_id=pk
        user=request.user
        organiazationunit=OrganiazationUnitRepo(user=user).organiazationunit(organiazationunit_id=organiazationunit_id)
        context=self.getManagerPageContext(request=request,page=organiazationunit)
        context['organiazationunit']=organiazationunit
        context['page']=organiazationunit
        return render(request,TEMPLATE_ROOT+'event.html',context)
    def contractor(self,request,pk,*args, **kwargs):
        contractor_id=pk
        user=request.user
        contractor=ContractorRepo(user=user).contractor(contractor_id=contractor_id)
        context=self.getManagerPageContext(request=request,page=contractor)
        context['contractor']=contractor
        context['page']=contractor
        return render(request,TEMPLATE_ROOT+'contractor.html',context)


