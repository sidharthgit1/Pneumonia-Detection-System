
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('logout/',views.logout),
    path('login_post/',views.login_post),
    path('admin_home/',views.admin_home),
    path('admin_change_password/',views.admin_change_password),
    path('admin_change_password_post/',views.admin_change_password_post),
    path('admin_view_review/',views.admin_view_review),
    path('admin_view_review_post/',views.admin_view_review_post),
    path('admin_view_rejected_doctor/',views.admin_view_rejected_doctor),
    path('admin_view_rejected_doctor_post/',views.admin_view_rejected_doctor_post),
    path('admin_view_feedback/',views.admin_view_feedback),
    path('admin_view_feedback_post/',views.admin_view_feedback_post),
    path('admin_view_doctor/',views.admin_view_doctor),
    path('admin_view_doctor_post/',views.admin_view_doctor_post),
    path('admin_view_approved_doctors/',views.admin_view_approved_doctors),
    path('admin_view_approved_doctors_post/',views.admin_view_approved_doctors_post),
    path('approved_doctors/<id>',views.approved_doctors),
    path('rejected_doctors/<id>', views.rejected_doctors),


    #####################################################################

    path('doctor_change_password/',views.doctor_change_password),
    path('doctor_add_schedule/',views.doctor_add_schedule),
    path('doctor_edit_profile/',views.doctor_edit_profile),
    path('doctor_edit_schedule/<id>',views.doctor_edit_schedule),
    path('doctor_delete_schedule/<id>',views.doctor_delete_schedule),
    path('doctor_signup/',views.doctor_signup),
    path('doctor_view_appointment/',views.doctor_view_appointment),
    path('doctor_view_profile/',views.doctor_view_profile),
    path('doctor_view_schedule/',views.doctor_view_schedule),
    path('doctor_xray__upload/<id>',views.doctor_xray__upload),
    path('doctor_edit_profile_post/',views.doctor_edit_profile_post),
    path('doctor_add_schedule_post/',views.doctor_add_schedule_post),
    path('doctor_change_password_post/',views.doctor_change_password_post),
    path('pnpreidct/',views.pnpreidct),
    path('doctor_edit_schedule_post/',views.doctor_edit_schedule_post),
    path('doctor_signup_post/', views.doctor_signup_post),
    path('doctor_view_schedule_post/', views.doctor_view_schedule_post),
    path('doctor_view_appointment_post/', views.doctor_view_appointment_post),
    path('doctor_home/',views.doctor_home),
    path('doctor_view_result/<id>',views.doctor_view_result),



    ####################################################################




    path('user_edit_profile/',views.user_edit_profile),
    path('user_edit_profile_post/',views.user_edit_profile_post),
    path('user_sign_up/',views.user_sign_up),
    path('user_sign_up_post/',views.user_sign_up_post),
    path('user_view_doctor/',views.user_view_doctor),
    path('user_view_doctor_post/',views.user_view_doctor_post),
    path('user_view_profile/',views.user_view_profile),
    path('user_view_profile_post/',views.user_view_profile_post),
    path('user_send_feedback/',views.user_send_feedback),
    path('user_send_review_about_doctor/<id>',views.user_send_review_about_doctor),
    path('user_view_appointment/',views.user_view_appointment),
    path('user_view_result/<id>',views.user_view_result),
    path('user_view_schedule/',views.user_view_schedule),
    path('user_send_feedback_post/',views.user_send_feedback_post),
    path('user_send_review_about_doctor_post/',views.user_send_review_about_doctor_post),
    path('user_view_appointment_post/',views.user_view_appointment_post),
    path('user_view_result_post/',views.user_view_result_post),
    path('user_view_schedule_post/',views.user_view_schedule_post),
    path('userhome/',views.userhome),
    path('user_change_password/',views.user_change_password),
    path('user_change_password_post/',views.user_change_password_post),
    path('pnpreidct/',views.pnpreidct),
    path('book_appointment/<id>',views.book_appointment),
    path('check_session/',views.check_session),





]

