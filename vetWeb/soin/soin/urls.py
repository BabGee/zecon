"""soin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from user import views as user_views
from portals import views as portal_views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('vet.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls, name='admin-vet'),
    #users sign up
    path('user/signup/vet_officer/', user_views.vet0fficer_signup_view, name='vet-register'),
    path('user/signup/farmer/',user_views.farmer_signup_view,name='farmer-register'),
    path('user/signup/student/',user_views.student_signup_view,name='student-register'),
    #users login 
    path('vet/login/',user_views.vet_login,name='vet-login'),
    path('farmer/login/',user_views.farmer_login,name='farmer-login'),
    path('student/login/',user_views.student_login,name='student-login'),
    path('logout/', user_views.user_logout, name='logout'),
    #password reset
    path("password-reset", auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),

    #users portals
    path('vet_portal/', portal_views.portal_vet, name='vet-portal'),
    path('farmer_portal/', portal_views.portal_farmer, name='farmer-portal'),
    path('student_portal/', portal_views.portal_student, name='student-portal'),
    #vet forms
    path('clinical_approach/',portal_views.clinical_approach,name='clinical-approach'),
    path('sick_approach', portal_views.sick_approach, name='sick-approach'),
    path('dead_approach', portal_views.dead_approach, name='dead-approach'),
    path('surgical_approach',portal_views.surgical_approach, name='surgical-approach'),
    path('deworming',portal_views.deworming,name='deworming'),
    path('vaccination',portal_views.vaccination,name='vaccination'),
    path('breeding_record/',portal_views.breeding_record,name='breeding_record'),
    path('artificial_insemination', portal_views.artificial_insemination, name='artificial-insemination'),
    path('pregnancy_diagnosis',portal_views.pregnancy_diagnosis,name='pregnancy_diagnosis'),
    path('calf_registration', portal_views.calf_registration, name='calf-registration'),
    path('livestock_inventory', portal_views.livestock_inventory, name='livestock-inventory'),
    path('consultation',portal_views.consultation,name='consultation'),
    #Farmer fetching forms pdf
    path('sickformpdf/', login_required(portal_views.Sick_Form_Pdf.as_view()), name='sickformpdf'),
    path('deadformpdf/', login_required(portal_views.Dead_Form_Pdf.as_view()), name='deadformpdf'),
    path('surgicalformpdf/', login_required(portal_views.Surgical_Form_Pdf.as_view()), name='surgicalformpdf'),
    path('dewormingformpdf/', login_required(portal_views.Deworming_Form_Pdf.as_view()), name='dewormingformpdf'),
    path('artificialformpdf/', login_required(portal_views.Artificial_Insemination_Form_Pdf.as_view()), name='artificialformpdf'),
    path('vaccinationformpdf/', login_required(portal_views.Vaccination_Form_Pdf.as_view()), name='vaccinationformpdf'),
    path('deadformpdf/', login_required(portal_views.Dead_Form_Pdf.as_view()), name='deadformpdf'),
    path('surgicalformpdf/', login_required(portal_views.Surgical_Form_Pdf.as_view()), name='surgicalformpdf'),
    path('dewormingformpdf/', login_required(portal_views.Deworming_Form_Pdf.as_view()), name='dewormingformpdf'),
    path('artificialformpdf/', login_required(portal_views.Artificial_Insemination_Form_Pdf.as_view()), name='artificialformpdf'),
    path('vaccinationpdf/', login_required(portal_views.Vaccination_Form_Pdf.as_view()), name='vaccinationformpdf'),
    path('consultationformpdf/', login_required(portal_views.Farm_Consultation_Form_Pdf.as_view()), name='consultationformpdf'),
    path('pregnancyformpdf/', login_required(portal_views.Pregnancy_Diagnosis_Form_Pdf.as_view()), name='pregnancyformpdf'),
    path('calfregformpdf/', login_required(portal_views.Calf_Registration_Form_Pdf.as_view()), name='calfregformpdf'),
    path('inventorypdf/', login_required(portal_views.Livestock_Form_Pdf.as_view()), name='inventoryformpdf'),
    path('gallerypdf/', portal_views.display_images, name='display-images')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)