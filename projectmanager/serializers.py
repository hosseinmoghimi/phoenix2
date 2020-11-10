from rest_framework import serializers 
from .models import *
from authentication.serializers import ProfileSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project        
        fields=['id','parent','color','get_absolute_url','get_resource','get_link','start_date','end_date','persian_start_date','persian_end_date','title','percent']
class ContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contractor        
        fields=['id','color','get_link','title','get_absolute_url']
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event        
        fields=['get_tag']
class EmployeeSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=Employee        
        fields=['id','role','get_absolute_url','profile']

class OrganizationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationUnit        
        fields=['id','title','employees_caption','get_link','parent_id','parent_title','caption']
class ArchiveDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['get_link']
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['color','get_absolute_url','title','id']