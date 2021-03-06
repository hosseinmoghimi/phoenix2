from django.urls import path
from . import views
from . import apis
from .apps import APP_NAME
from app import views as app_views
app_name=APP_NAME
urlpatterns=[
    path('',views.BasicViews().home,name='home'),
    path('search/',views.BasicViews().search,name='search'),
    path('pages/timeline/',views.PagesViews().timeline,name='pages_timeline'),
    path('components/notifications/',views.ComponentsViews().notifications,name='components_notifications'),
    path('components/buttons/',views.ComponentsViews().buttons,name='components_buttons'),
    path('components/panels/',views.ComponentsViews().panels,name='components_panels'),
    path('components/alerts/',views.ComponentsViews().alerts,name='components_alerts'),
    path('calendar/',views.BasicViews().calendar,name='calendar'),
    path('wizard/',views.BasicViews().wizard,name='wizard'),
    path('widgets/',views.BasicViews().widgets,name='widgets'),
    path('charts/',views.BasicViews().charts,name='charts'),
    path('tables/regular/',views.TablesViews().regular,name='tables_regular'),
    path('blog/<int:pk>/',app_views.PageViews().blog,name='blog'),
    path('resume/<int:pk>/',app_views.PageViews().resume,name='resume'),
    path('ourwork/<int:pk>/',app_views.PageViews().ourwork,name='ourwork'),
    path('feature/<int:pk>/',app_views.PageViews().feature,name='feature'),
    path('notifications/',views.ProfileViews().notifications,name='notifications'),
    path('notification/<int:pk>/',views.ProfileViews().notification,name='notification'),
    path('remove_tag/',apis.PageViews().remove_tag,name='remove_tag'),
    path('add_tag/',apis.PageViews().add_tag,name='add_tag'),
    path('add_link/',apis.PageViews().add_link,name='add_link'),
    path('add_image/',apis.PageViews().add_image,name='add_image'),
    path('add_comment/',apis.PageViews().add_comment,name='add_comment'),
    path('add_resume/',apis.PageViews().add_resume,name='add_resume'),
    path('add_resume_category/',apis.PageViews().add_resume_category,name='add_resume_category'),
    path('delete_comment/',apis.PageViews().delete_comment,name='delete_comment'),
    path('download/<int:document_id>/',views.BasicViews().download,name='download'),
    path('add_document/',apis.PageViews().add_document,name='add_document'),
    path('document/<int:pk>/',views.BasicViews().download,name='document'),
    path('my_notifications/',apis.BasicViews().my_notifications,name='my_notifications'),
    path('profile_customization/',apis.ProfileViews().profile_customization,name='profile_customization'),
]