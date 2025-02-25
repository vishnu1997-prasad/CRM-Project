from django.urls import path

from . import views

urlpatterns = [

    path('dash',views.DashBoardView.as_view(),name = 'dashboard'),
    path('students-list/',views.StudentsListView.as_view(),name='students-list'),
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('student_detail/<str:uuid>/',views.StudentDetailView.as_view(),name='student_detail'),
    path('student-delete/<str:uuid>/',views.StudentDeleteView.as_view(),name='student-delete'),
    path('student-update/<str:uuid>/',views.StudentUpdateView.as_view(),name='student-update'),

]
