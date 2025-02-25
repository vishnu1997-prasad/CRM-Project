from django.db import models
import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        abstract = True


class CourseChoice(models.TextChoices):

    # variable = database value, representation

    PY_DJANGO = 'PY-DJANGO', 'PY-DJANGO'

    MEARN = 'MEARN', 'MEARN'

    DATA_SCIENCE = 'DATA_SCIENCE', 'DATA_SCIENCE'

    SOFTWARE_TESTING = 'SOFTWARE_TESTING','SOFTWARE_TESTING'

class DistrictChoice(models.TextChoices):

    THIRUVANANTHAPURAM = 'THIRUVANANTHAPURAM', 'THIRUVANANTHAPURAM'

    KOLLAM = 'KOLLAM', 'KOLLAM'
    
    PATHANAMTHITTA = 'PATHANAMTHITTA', 'PATHANAMTHITTA'

    ALAPPUZHA = 'ALAPPUZHA', 'ALAPPUZHA'

    KOTTAYAM = 'KOTTAYAM', 'KOTTAYAM'

    IDUKKI  = 'IDUKKI', 'IDUKKI'

    ERNAKULAM = 'ERNAKULAM', 'ERNAKULAM'

    THRISSUR = 'THRISSUR', 'THRISSUR'

    PALAKKAD = 'PALAKKAD', 'PALAKKAD'

    MALAPPURAM = 'MALAPPURAM', 'MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE', 'KOZHIKODE'

    WAYANAD = 'WAYANAD', 'WAYANAD'

    KANNUR = 'KANNUR','KANNUR'

    KASARAGOD = 'KASARAGOD' ,'KASARAGOD'


class BatchChoice(models.TextChoices):


    PY_1 = 'PY-NOV-2024', 'PY-NOV-2024'

    PY_2 = 'PY-JAN-2025', 'PY-JAN-2025'

    MEARN_1 = 'MEARN-NOV-2024', 'MEARN-NOV-2024'

    MEARN_2 = 'MEARN-JAN-2025', 'MEARN-JAN-2025'

    DATA_SCIENCE = 'DS-JAN-2025', 'DS-JAN-2025'

    SOFTWARE_TESTING = 'ST-JAN-2025','ST-JAN-2025'


class TrainerChoice(models.TextChoices):

    PYTHON = 'JOHN DOE', 'JOHN DOE'

    MEARN = 'JAMES', 'JAMES'

    SW_TESTING = 'PETER', 'PETER'

    DATA_SCIENCE = 'ALEX', 'ALEX'


class Students(BaseClass):

    # name = models.CharField(max_length=50)

    # adm_number = models.CharField(max_length=50)

    # email = models.EmailField()

    # contact = models.CharField(max_length=15)

    # address = models.TextField()

    # course = models.CharField()

    # batch = models.CharField()

    # join_date = models.DateField()
 
 
    # Personal details fields

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20)

    last_name = models.CharField(max_length=20)

    photo = models.ImageField(upload_to='students')

    email = models.EmailField(unique=True)

    contact_num = models.CharField(max_length=15)

    house_name = models.CharField(max_length=50)

    post_office = models.CharField(max_length=30)

    district = models.CharField(max_length=30, choices=DistrictChoice.choices)

    pincode = models.CharField(max_length=6)


    # course details

    adm_num = models.CharField(max_length=20)

    # course = models.CharField(max_length=20, choices=CourseChoice.choices) #default=CourseChoice.PY_DJANGO

    course = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    # batch = models.CharField(max_length=25, choices=BatchChoice.choices)

    batch = models.ForeignKey('batches.Batches',null=True,on_delete=models.SET_NULL)

    # batch_date = models.DateField()

    join_date = models.DateField(auto_now_add=True)

    # trainer_name = models.CharField(max_length=30, choices=TrainerChoice.choices)

    trainer = models.ForeignKey('trainers.Trainers',null=True,on_delete=models.SET_NULL)


    def __str__(self):

        return f'{self.first_name} {self.last_name} {self.batch}'
    
    class Meta :

        verbose_name = 'Students'

        verbose_name_plural = 'Interns'

        ordering = ['id']





