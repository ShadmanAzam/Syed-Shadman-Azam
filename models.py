from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(max_length=50)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True"))

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL, related_name="users")

    def __str__(self):
        return self.email

class Stack_holder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=100)

class Designation(models.Model):
    name = models.CharField(max_length=100)
    dep_id = models.IntegerField()

class Employee(models.Model):
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="employees")
    job_title = models.CharField(max_length=100)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="employee_profile")
    phone_no = models.CharField(max_length=50)

class Incident_type(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.ManyToManyField(Department, related_name="incident_types")

class Improvement_recommendation(models.Model):
    action_title = models.CharField(max_length=100)
    action_description = models.CharField(max_length=50)
    responsible_employee_id = models.ManyToManyField(Employee, related_name="recommendations")
    incident_id = models.IntegerField()

class Department_poc(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="pocs")
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="department_pocs")

class Incident_ticket(models.Model):
    Assigned_poc = models.ForeignKey(Department_poc, on_delete=models.CASCADE, related_name="assigned_incidents")
    report_type = models.ForeignKey(Incident_type, on_delete=models.CASCADE, related_name="incidents")
    requestor_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="requested_tickets")
    occurance_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateField(auto_now=True, null=True)
    facilty = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    potential_severity = models.CharField(null=True, max_length=50)
    likelihood_of_recurrance = models.CharField(null=True, max_length=50)
    risk_level = models.CharField(null=True, max_length=50)

class Contributing_factor(models.Model):
    name = models.CharField(max_length=50)

class Incident_factor(models.Model):
    factor_id = models.ForeignKey(Contributing_factor, on_delete=models.CASCADE, related_name="incident_factors")
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE, related_name="incident_factors")

class Incident_evidence(models.Model):
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE, related_name="evidences")
    file = models.FileField(upload_to=None, max_length=100, null=True)

class Status(models.Model):
    name = models.CharField(max_length=50)

class Incident_status(models.Model):
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Follow_up(models.Model):
    date_completed = models.DateField(auto_now_add=True)
    action_title = models.CharField(max_length=100)
    action_description = models.CharField(max_length=100)
    responsible_employee_id = models.ManyToManyField(Employee, related_name="follow_ups")
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE, related_name="follow_ups")

class Incident_witness(models.Model):
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE, related_name="witnesses")
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="witnessed_incidents")

class Individuals_involved(models.Model):
    incident_id = models.ForeignKey(Incident_ticket, on_delete=models.CASCADE, related_name="involved_individuals")
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="incidents_involved")

class Immediate_action(models.Model):
    incident_id = models.ManyToManyField(Incident_ticket, related_name="immediate_actions")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    employee_id = models.ManyToManyField(Employee, related_name="immediate_actions")

class Immediate_action_employee(models.Model):
    immediate_action_id = models.ManyToManyField(Immediate_action, related_name="assigned_employees")
    employee_id = models.ManyToManyField(Employee, related_name="immediate_action_roles")