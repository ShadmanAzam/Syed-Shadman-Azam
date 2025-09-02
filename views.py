from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
# Create your views here.

class MyuserViewSet(ModelViewSet):
    queryset=MyUser.objects.all()
    serializer_class=Myuserserilizer
    
class DepartmentViewSet(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=Departmentserilizer
    
class  Incident_typeViewSet(ModelViewSet):
    queryset=Incident_type.objects.all()
    serializer_class=Incident_typeserializer
    
    
class Department_pocViewSet(ModelViewSet):
    queryset=Department_poc.objects.all()
    serializer_class=Department_pocserilizer

class  Incident_evidenceViewSet(ModelViewSet):
    queryset=Incident_evidence.objects.all()
    serializer_class=Incident_evidenceserilizer

    
class Incident_ticketViewSet(ModelViewSet):
    queryset=Incident_ticket.objects.all()
    serializer_class=Incident_ticketserilizer

class StatusViewSet(ModelViewSet):
    queryset=Status.objects.all()
    serializer_class=Statusserilizer
    
class Incident_statusViewSet(ModelViewSet):
    queryset=Incident_status.objects.all()
    serializer_class=Incident_statusserilizer
    
class Follow_upserilizerViewSet(ModelViewSet):
    queryset=Follow_up.objects.all()
    serializer_class=Follow_upserilizer

class Incident_witnessViewSet(ModelViewSet):
    queryset=Incident_witness.objects.all()
    serializer_class=Incident_witnessserilizer
    
class Individuals_involvedViewSet(ModelViewSet):
    queryset=Individuals_involved.objects.all()
    serializer_class=Individuals_involvedserilizer
    
class Immediate_actionViewSet(ModelViewSet):
    queryset=Immediate_action.objects.all()
    serializer_class=Immediate_actionserilizer
    
class Immediate_action_employeeViewSet(ModelViewSet):
    queryset=Immediate_action_employee.objects.all()
    serializer_class=Immediate_action_employeeserializer



class Follow_upViewSet(ModelViewSet):
    queryset=Follow_up.objects.all()
    serializer_class=Follow_upserilizer





class Register_user(APIView):
     
   def get(self ,request):
       obj=Employee.objects.all()
       ser=Employeeserializer(obj,many=True)
       return Response(ser.data)
   
   def post(self,request):
       data=request.data
       employ={}
       employ["designation_id"] = data.pop("designation_id", None)
       employ["job_title"] = data.pop("job_title", None)
       employ["phone_no"] = data.pop("phone_no", None)
       ser=Myuserserilizer(data=data)
       if ser.is_valid():
          user= ser.save()
          employ["user_id"]=user.id
          ser=Employeeserializer(data=employ)
          if ser.is_valid():
              ser.save()
              return Response({"massage":"Register Successfully"})
          else:
              return Response(ser.errors)
       else:
            return Response(ser.errors)  
          
           
       
       
       
        



