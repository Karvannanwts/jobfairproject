"""
URL configuration for jobfairproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home_view,name = 'home'),
    # #path('login',views.login,name='login'),
    # path('signin',views.signin,name='signin'),
    # path('register_email',views.register,name='register_email'),
    # path('email_otp',views.otp,name='email_otp'),
    # path('register_details',views.register_details,name="register_details"),
    # path('register_details2',views.register_details2,name='register_details2'),
    path('students_corner',views.student_corner,name="students_corner"),
    path('college_registration',views.college_registration,name='college_registration'),
    # path('register-new-college/', views.register_new_college, name='register_new_college'),
    # path('registered_college_login', views.registered_college_login, name='registered_college_login'),
    # path('submit_college_details', views.submit_college_details, name='submit_college_details'),
    # path('personal_details', views.personal_details, name='personal_details'),
    # path('aadhar', views.aadhar, name='aadhar'),
    path('personal_1', views.personal_1, name='personal_1'),
    path('academic', views.academic, name='academic'),
    path('academic_qualification', views.academic_qualification, name='academic_qualification'),
    path('academic_graduate', views.academic_graduate, name='academic_graduate'),
    path('academic_xii_grade', views.academic_xii_grade, name='academic_xii_grade'),
    path('academic_x_grade', views.academic_x_grade, name='academic_x_grade'),
    path('other_details', views.other_details, name='other_details'),
    path('other_qualificaion', views.other_qualificaion, name='other_qualificaion'),
    path('work_exp', views.work_exp, name='work_exp'),
    path('arrear', views.arrear, name='arrear'),
    path('resume', views.resume, name='resume'),
    # path('admin_login',views.admin_login,name="admin_login"),
    path('preview',views.preview,name="preview"),
    path('reg',views.reg,name="reg"),
    # path('send-otp/', views.send_otp_view, name='send_otp'),
    # path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('reg_login', views.reg_login, name='reg_login'),
    path('reg_otp', views.reg_otp, name='reg_otp'),
    path('payment',views.payment,name='payment'),
    path('college_preview',views.college_preview,name='college_preview'),
    path('student_preview',views.student_preview,name='student_preview'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
