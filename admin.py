from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Role)
admin.site.register(Stack_holder)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Incident_type)
admin.site.register(Improvement_recommendation)
admin.site.register(Department_poc)
admin.site.register(Incident_ticket)
admin.site.register(Contributing_factor)
admin.site.register(Incident_factor)
admin.site.register(Incident_evidence)
admin.site.register(Status)
admin.site.register(Incident_status)
admin.site.register(Follow_up)
admin.site.register(Incident_witness)
admin.site.register(Individuals_involved)
admin.site.register(Immediate_action)
admin.site.register(Immediate_action_employee)