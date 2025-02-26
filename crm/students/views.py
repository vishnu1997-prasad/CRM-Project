from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import DistrictChoice,CourseChoice,TrainerChoice,BatchChoice
from .utility import get_admission_num,get_password
from .models import Students
from django.db import transaction
from .forms import StudentRegisterForm
from django.db.models import Q
from authentication.models import Profile 

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.permissions import permission_roles
# Create your views here.


class GetStudentObject() :

    def get_student(self,request,uuid):


        try :

            student = Students.objects.get(uuid=uuid)

            return student

        except :

            return render(request,'error_pages/error-404.html')
        

# @method_decorator(login_required(login_url='login'),name='dispatch')   

# @method_decorator(permission_roles(roles = ['Admin','Sales']),name = 'dispatch')     
class DashBoardView(View) :

    def get(self,request,*args,**kwargs):

        return render(request,'students/dashboard.html')
    
# roles admin,sales,academic counselor,trainer
    
@method_decorator(permission_roles(roles = ['Admin','Sales','Trainer','Academic Counselor']),name = 'dispatch') 
class StudentsListView(View) :

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        role = request.user.role

        if role in ['Trainer'] :

            students = Students.objects.filter(active_status = True,trainer__profile = request.user)

            if query :

                students = Students.objects.filter(Q(active_status=True)&Q(trainer__profile = request.user)&(Q(first_name__icontains=query)|Q(last_name__icontains = query)|Q(house_name__icontains=query)|
                                                                      
                                                                      Q(contact_num__icontains = query)|Q(pincode__icontains = query)|Q(post_office__icontains = query)|
                                                                      
                                                                      Q(email__icontains = query)|Q(course__name__icontains = query)|Q(district__icontains = query)
                                                                     
                                                                      |Q(batch__name__icontains = query)|Q(trainer__first_name__icontains = query)))


        else :

            students = Students.objects.filter(active_status = True)


            if query :

                students = Students.objects.filter(Q(active_status=True)&(Q(first_name__icontains=query)|Q(last_name__icontains = query)|Q(house_name__icontains=query)|
                                                                      
                                                                      Q(contact_num__icontains = query)|Q(pincode__icontains = query)|Q(post_office__icontains = query)|
                                                                      
                                                                      Q(email__icontains = query)|Q(course__name__icontains = query)|Q(district__icontains = query)
                                                                     
                                                                      |Q(batch__name__icontains = query)|Q(trainer__first_name__icontains = query)))
        # students = Students.objects.all()

        
        data = {'students' : students,'query' : query}

        return render(request,'students/students_list.html', context=data)
    
# roles admin,sales
@method_decorator(permission_roles(roles = ['Admin','Sales']),name = 'dispatch') 

class RegistrationView(View) :

    
    def get(self,request,*args,**kwargs):

        form = StudentRegisterForm()

        # data = {'districts' : DistrictChoice, 'courses' : CourseChoice,'batches':BatchChoice, 'trainers' :TrainerChoice, 'form':form}

        data = {'form':form}

        
        
        return render(request,'students/registration.html', context=data)

    def post(self,request,*args,**kwargs):

        form = StudentRegisterForm(request.POST,request.FILES)

        if form.is_valid():

            with transaction.atomic():

                student = form.save(commit=False)

                student.adm_num = get_admission_num()

                # student.join_date = '2024-02-05'

                username = student.email

                password = get_password()

                print(password)

                profile = Profile.objects.create_user(username=username,password=password, role = 'Student' )

                student.profile = profile    # zlPSFMIA

                student.save()

            return redirect('students-list')
        
        else :            
            
            data = {'form':form}

            return render (request,'students/registration.html',context=data)
        
@method_decorator(permission_roles(roles = ['Admin','Sales','Trainer','Academic Counselor']),name = 'dispatch') 
class StudentDetailView(View) :

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        # student = get_object_or_404(Students,pk=pk)   simple method instead of try except

        student = GetStudentObject().get_student(request,uuid)

        data = {'student':student}

        return render(request,'students/student-detail.html',context=data)

            
@method_decorator(permission_roles(roles = ['Admin','Sales']),name = 'dispatch') 
    
class StudentDeleteView(View) :

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)
        
        # student.delete()

        student.active_status = False

        student.save()

        return redirect('students-list')
    

@method_decorator(permission_roles(roles = ['Admin','Sales']),name = 'dispatch') 

class StudentUpdateView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegisterForm(instance=student)

        data = {'form': form}

        return render(request,'students/student_update.html',context=data)
    
    def post(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegisterForm(request.POST,request.FILES,instance=student)

        if form.is_valid():

            form.save()

            return redirect('students-list')
        
        else :

            data = {'form' :form}

            return render(request,'students/student_update.html',context=data)









        # form_data = request.POST

        # first_name = form_data.get("first_name")
        
        # last_name = form_data.get("last_name")

        # photo = request.FILES.get("photo")
        
        # email = form_data.get("email")
       
        # contact_number = form_data.get("phone")
       
        # house_name = form_data.get("house_name")
       
        # post_office = form_data.get("post_office")
       
        # pincode = form_data.get("pincode")
       
        # course = form_data.get("course")
       
        # district = form_data.get("district")
       
        # batch = form_data.get("batch")
       
        # batch_date = form_data.get("batch_date")
       
        # trainer = form_data.get("trainer")

        # admsn_num = get_admission_num()

        # join_date = '2024-08-16'

        # Students.objects.create(first_name=first_name,last_name=last_name,photo=photo,
        #                         email=email,contact_num=contact_number,house_name=house_name,
        #                         post_office=post_office,district=district,pincode=pincode,
        #                         course=course,batch=batch,batch_date=batch_date,trainer_name=trainer,
        #                         adm_num=admsn_num,join_date=join_date)

       
        
        # context={'first_name':first_name,
        #             'last_name':last_name,'photo':photo,'email':email,'phone':contact_number,
        #             'house_name':house_name,'post_office':post_office,'pincode':pincode,'course':course,
        #             'district':district,'batch':batch,'batch_date':batch_date,'trainer':trainer}

