from django.urls import path

from . import views

urlpatterns = [

    path('student_payment/',views.StudentPaymentView.as_view(),name='student_payment'),
    
    path('razorpay/',views.RazorpayView.as_view(),name='razorpay'),

    path('payment-verify/',views.PaymentVerifyView.as_view(),name='payment-verify'),
]