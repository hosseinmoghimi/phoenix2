from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from dashboard.enums import *
from dashboard.forms import AddTagForm,AddDocumentForm,AddCommentForm,AddLinkForm,AddImageForm
from dashboard.serializers import TagSerializer,DocumentSerializer,CommentSerializer,LinkSerializer,GalleryPhotoSerializer
from .forms import *
from authentication.repo import ProfileRepo
from dashboard.views import getContext as DashboardContext
from dashboard.utils import AdminUtility

import json
TEMPLATE_ROOT='material/'




def getContext(request):
    user=request.user
    context=DashboardContext(request)
    parameter_repo=ParameterRepo(user=request.user)
    main_pic_repo=MainPicRepo(user=request.user)
    link_repo=LinkRepo(user=request.user)
    context['app']={
        'theme_color':parameter_repo.get(ParametersEnum.THEME_COLOR),
        'nav_items':link_repo.get_nav_items(),
        'about_us_short':parameter_repo.get(ParametersEnum.ABOUT_US_SHORT),
        'GOOGLE_SEARCH_CONSOLE_TAG':parameter_repo.get(ParametersEnum.GOOGLE_SEARCH_CONSOLE_TAG),
        'NAV_TEXT_COLOR':parameter_repo.get(ParametersEnum.NAV_TEXT_COLOR),
        'NAV_BACK_COLOR':parameter_repo.get(ParametersEnum.NAV_BACK_COLOR),
        'slogan':parameter_repo.get(ParametersEnum.SLOGAN),
        'logo':main_pic_repo.get(name=MainPicEnum.LOGO),
        'favicon':main_pic_repo.get(name=MainPicEnum.FAVICON),
        'loading':main_pic_repo.get(name=MainPicEnum.LOADING),
        'pretitle':parameter_repo.get(ParametersEnum.PRE_TILTE),
        'title':parameter_repo.get(ParametersEnum.TITLE),
        'address':parameter_repo.get(ParametersEnum.ADDRESS),    
        'mobile':parameter_repo.get(ParametersEnum.MOBILE),           
        'email':parameter_repo.get(ParametersEnum.EMAIL),      
        'tel':parameter_repo.get(ParametersEnum.TEL),
        'url':parameter_repo.get(ParametersEnum.URL),
        'meta_data_items':MetaDataRepo().list_for_home(),
        'our_team_title':OurTeamRepo(user=user).get_title(),
        'our_team_link':OurTeamRepo(user=user).get_link(),
    }
    context['admin_utility']=AdminUtility(app_name=APP_NAME)
    return context

class BasicViews(View):
    def contact(self,request,*args, **kwargs):
        context=getContext(request)
        context['body_class']='contact-page'
        context['add_contact_message_form']=AddContactMessageForm()
        return render(request,TEMPLATE_ROOT+'contact.html',context)

    def about(self,request,*args, **kwargs):
        context=getContext(request)
        user=request.user
        context['body_class']='about-us'
        context['about_header']=MainPicRepo(user=user).get(MainPicEnum.ABOUT_HEADER)
        context['about_text']=ParameterRepo(user=user).get(ParametersEnum.ABOUT_US_TITLE)
        return render(request,TEMPLATE_ROOT+'about.html',context)

    def home(self,request,*args,**kwargs):
        user=request.user
        context=getContext(request)
        homesliders=HomeSliderRepo(user=user).list()
        context['homesliders']=homesliders
        features=FeatureRepo(user=user).list_for_home()
        context['features']=features
        blogs=BlogRepo(user=user).list_for_home()
        context['blogs']=blogs
        ourworks=OurWorkRepo(user=user).list_for_home()
        context['ourworks']=ourworks
        ourteams=OurTeamRepo(user=user).list()
        context['ourteams']=ourteams
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
        return render(request,TEMPLATE_ROOT+'examples/all-components.html',context)
    def sections(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/sections.html',context)


class PageViews(View):
    def getPageContext(self,request,page,*args, **kwargs):
        context=getContext(request)

        context['add_tag_form']=AddTagForm()
        context['add_link_form']=AddLinkForm()
        context['add_document_form']=AddDocumentForm()
        context['add_image_form']=AddImageForm()
        context['add_comment_form']=AddCommentForm()
        comments_s=json.dumps(CommentSerializer(page.comments.all(),many=True).data)
        context['comments_s']=comments_s
        context['images_s']=json.dumps(GalleryPhotoSerializer(page.images.all(),many=True).data)
        context['tags_s']=json.dumps(TagSerializer(page.tags.all(),many=True).data)
        context['links_s']=json.dumps(LinkSerializer(page.links.all(),many=True).data)
        context['documents_s']=json.dumps(DocumentSerializer(page.documents.all(),many=True).data)
        
        return context

    def resume(self,request,pk,*args, **kwargs):
        user=request.user
        resume=ResumeRepo(user=user).resume(resume_id=pk)
        context=self.getPageContext(request=request,page=resume)        
        context['page']=resume
        context['resume']=resume
        return render(request,TEMPLATE_ROOT+'resume.html',context)
    def blog(self,request,pk,*args, **kwargs):
        user=request.user
        blog=BlogRepo(user=user).blog(blog_id=pk)
        context=self.getPageContext(request=request,page=blog)
        context['page']=blog
        context['blog']=blog
        return render(request,TEMPLATE_ROOT+'blog.html',context)
    def feature(self,request,pk,*args, **kwargs):
        user=request.user        
        feature=FeatureRepo(user=user).feature(feature_id=pk)
        context=self.getPageContext(request=request,page=feature)  
        context['page']=feature
        context['feature']=feature
        return render(request,TEMPLATE_ROOT+'feature.html',context)
    def ourwork(self,request,pk,*args, **kwargs):
        user=request.user
        ourwork=OurWorkRepo(user=user).ourwork(ourwork_id=pk)
        context=self.getPageContext(request=request,page=ourwork) 
        context['page']=ourwork
        context['ourwork']=ourwork
        return render(request,TEMPLATE_ROOT+'ourwork.html',context)

# Create your views here.
