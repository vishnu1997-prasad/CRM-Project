# crone to send reminder about payment

from .models import Payment

from django.utils import timezone

import threading

from students.utility import send_email

from apscheduler.schedulers.background import BackgroundScheduler

def reminder_email() :

    current_date = timezone.now().date()

    five_days_before_date = current_date - timezone.timedelta(days=5)

    pending_payments = Payment.objects.filter(status = 'Pending',student__join_date__lte = five_days_before_date)

    if pending_payments.exists():

        # sending payment reminder email to students mail id
                
        for payment in pending_payments :
                
                subject = 'Payment Reminder'

                recepients = [payment.student.email]

                template = 'email/payment-reminder.html'
                
                context = {'name' : f'{payment.student.first_name} {payment.student.last_name}'}

                thread = threading.Thread(target = send_email,args=(subject,recepients,template,context))

                thread.start()

        print('all mail send')

            


#apscheduler

#add_job(task_function,trigger)   add_job parameters


def scheduler_start() :
     
     scheduler = BackgroundScheduler()

     scheduler.add_job(reminder_email,'cron',hour = 10,minute=0)

     scheduler.start()

