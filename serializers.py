from .models import *
from rest_framework import serializers


class Myuserserilizer(serializers.ModelSerializer):
    
  class Meta:
      model=MyUser
      fields="__all__"
      
class Employeeserializer(serializers.ModelSerializer):
     class Meta:
         model=Employee
         fields="__all__"

class Incident_typeserializer(serializers.ModelSerializer):
      class Meta:
            model=Incident_type
            fields="__all__"
            
class Improvement_recommendationserilizer(serializers.ModelSerializer):
      class Meta:
            model=Improvement_recommendation
            fields="__all__"

class Department_pocserilizer(serializers.ModelSerializer):
      class Meta:
            model=Department_poc
            fields="__all__"

class Departmentserilizer(serializers.ModelSerializer):
      class Meta:
            model=Department
            fields="__all__"

class Incident_typeserilizer(serializers.ModelSerializer):
      class Meta:
            model=Incident_type
            fields="__all__"

class Incident_evidenceserilizer(serializers.ModelSerializer):
      class Meta:
            model=Incident_evidence
            fields="__all__"

class Statusserilizer(serializers.ModelSerializer):
      class Meta:
            model=Status
            fields="__all__"

class Statusserilizer(serializers.ModelSerializer):
      class Meta:
            model=Status
            fields="__all__"
            
class Incident_statusserilizer(serializers.ModelSerializer):
      class Meta:
            model=Incident_status
            fields="__all__"

class Follow_upserilizer(serializers.ModelSerializer):
      class Meta:
            model=Follow_up
            fields="__all__"
      
class Incident_witnessserilizer(serializers.ModelSerializer):
      class Meta:
            model=Incident_witness
            fields="__all__"
            
class Individuals_involvedserilizer(serializers.ModelSerializer):
      class Meta:
            model=Individuals_involved
            fields="__all__"

class Immediate_actionserilizer(serializers.ModelSerializer):
      class Meta:
            model=Immediate_action
            fields="__all__"

class Immediate_action_employeeserializer(serializers.ModelSerializer):
      class Meta:
            model=Immediate_action_employee
            fields="__all__"
            
class Incident_ticketserilizer(serializers.ModelSerializer):

      class Meta:
            model=Incident_ticket
            fields="__all__"
      
         
         
       


    
