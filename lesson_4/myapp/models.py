# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.TextField()
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.country_name


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.TextField()
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departments'

    def __str__(self):
        return self.department_name

class Dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    relationship = models.TextField()
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dependents'

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField(blank=True, null=True)
    hire_date = models.TextField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.TextField()  # This field type is a guess.
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.TextField()
    min_salary = models.TextField()  # This field type is a guess.
    max_salary = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jobs'

    def __str__(self):
        return self.job_title

class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField()
    state_province = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'regions'

    def __str__(self):
        return self.region_name