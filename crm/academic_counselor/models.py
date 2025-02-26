from django.db import models

from students.models import BaseClass,DistrictChoice

# Create your models here.

class AcademicCounselor(BaseClass):

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    employee_id = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='academic-counselor')

    email = models.EmailField()

    contact = models.CharField(max_length=13)

    house_name = models.CharField(max_length=25)

    post_office = models.CharField(max_length=25)

    district = models.CharField(max_length=20,choices=DistrictChoice.choices)

    pincode = models.CharField(max_length=6)

    qualification = models.CharField(max_length=25)
    
    stream = models.CharField(max_length=25)

    id_proof = models.FileField(upload_to='acdemic-counselor/idproof')


    def __str__(self):

        return f'{self.first_name} {self.employee_id}'
    
    class Meta:

        verbose_name = 'Academic Counselor'

        verbose_name_plural = 'Academic Counselor'
