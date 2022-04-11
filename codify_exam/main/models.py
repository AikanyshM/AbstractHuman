from django.db import models
from datetime import date
from django.urls import reverse

class AbstractHuman(models.Model):
    fullname = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.fullname

    def get_age(self):
        age = date.today().year - self.birth_date.year
        return age

class Worker(AbstractHuman):
    work_position = models.CharField(max_length=30)
    work_experience = models.DateField()

    def __str__(self):
        return self.work_position
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('worker_detail', kwargs={'pk': self.id})

class Document(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    card_id = models.CharField(max_length=10)

    def __str__(self):
        return self.worker.fullname
    
    def save(self, *args, **kwargs):
        print(f'{self.worker.fullname} has been saved!')
        super().save(*args, **kwargs)

class Project(models.Model):
    project_name = models.CharField(max_length=15)
    members = models.ManyToManyField(Worker, through="Membership")

    def __str__(self):
        return self.project_name

class Membership(models.Model):
    employee = models.ForeignKey(Worker, on_delete=models.CASCADE)
    workproject = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return self.employee.name

class Customer(AbstractHuman):
    address = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.fullname

class VIPCustomer(Customer):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def __str__(self):
        return self.vip_status_start    

