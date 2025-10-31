
from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static

from .import views,HOD_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    #login path
    path('', views.LOGIN,name='login'),#main page is login when removed '/login' and keeping it blank
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    #profile update
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    #this is hod panel
    path('HOD/Home', HOD_views.HOME,name='hod_home'),
    path('HOD/Student/Add',HOD_views.ADD_STUDENT,name='add_student'),
    path('HOD/Student/View',HOD_views.VIEW_STUDENT,name='view_student'),
    path('HOD/Student/Edit/<str:id>',HOD_views.EDIT_STUDENT,name='edit_student'),
    path('HOD/Student/Update',HOD_views.UPDATE_STUDENT,name='update_student'),
    path('HOD/Student/Delete/<str:admin>',HOD_views.DELETE_STUDENT,name='delete_student'),

    path('HOD/Staff/Add',HOD_views.ADD_STAFF,name='add_staff'),
    path('HOD/Staff/View',HOD_views.VIEW_STAFF,name='view_staff'),
    path('HOD/Staff/Edit/<str:id>',HOD_views.EDIT_STAFF,name='edit_staff'),
    path('HOD/Staff/Update',HOD_views.UPDATE_STAFF,name='update_staff'),
    path('HOD/Staff/Delete/<str:admin>',HOD_views.DELETE_STAFF,name='delete_staff'),


    path('HOD/Course/Add',HOD_views.ADD_COURSE,name='add_course'),
    path('HOD/Course/View',HOD_views.VIEW_COURSE,name='view_course'),
    path('HOD/Course/Edit/<str:id>',HOD_views.EDIT_COURSE,name='edit_course'),
    path('HOD/Course/Update',HOD_views.UPDATE_COURSE,name='update_course'),
    path('HOD/Course/Delete/<str:id>',HOD_views.DELETE_COURSE,name='delete_course'),

    path('HOD/Subject/Add',HOD_views.ADD_SUBJECT,name='add_subject'),
    path('HOD/Subject/View',HOD_views.VIEW_SUBJECT,name='view_subject'),
    path('HOD/Subject/Edit/<str:id>',HOD_views.EDIT_SUBJECT,name='edit_subject'),
    path('HOD/Subject/Update',HOD_views.UPDATE_SUBJECT,name='update_subject'),
    path('HOD/Subject/Delete/<str:id>',HOD_views.DELETE_SUBJECT,name='delete_subject'),

    path('HOD/Session/Add',HOD_views.ADD_SESSION,name='add_session'),
    path('HOD/Session/View',HOD_views.VIEW_SESSION,name='view_session'),
    path('HOD/Session/Edit/<str:id>',HOD_views.EDIT_SESSION,name='edit_session'),
    path('HOD/Session/Update',HOD_views.UPDATE_SESSION,name='update_session'),
    path('HOD/Session/Delete/<str:id>',HOD_views.DELETE_SESSION,name='delete_session'),

    path('HOD/Staff/Send_Notification',HOD_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('HOD/Staff/save_Notification',HOD_views.STAFF_SAVE_NOTIFICATION,name='save_staff_notification'),

    path('HOD/Student/Send_Notification',HOD_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('HOD/Student/save_Notification',HOD_views.STUDENT_SAVE_NOTIFICATION,name='save_student_notification'),


    path('HOD/Staff/Leave_view',HOD_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('HOD/Staff/approve_leave/<str:id>',HOD_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('HOD/Staff/disapprove_leave/<str:id>',HOD_views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),

    path('HOD/Student/Leave_view',HOD_views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('HOD/Student/approve_leave/<str:id>',HOD_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('HOD/Student/disapprove_leave/<str:id>',HOD_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),

    path('HOD/Staff/feedback',HOD_views.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('HOD/Staff/feedback/save',HOD_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_reply_save'),

    path('HOD/Student/feedback',HOD_views.STUDENT_FEEDBACK,name='get_student_feedback'),
    path('HOD/Student/feedback/save',HOD_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_reply_save'),

    path('HOD/View_Attendance',HOD_views.VIEW_ATTENDANCE,name='view_attendance'),

    #this is staff panel
    path('Staff/Home', Staff_views.HOME,name='staff_home'),


    path('Staff/Notifications',Staff_views.NOTIFICATIONS,name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),

    path('Staff/Apply_leave',Staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_leave_Save',Staff_views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/Feedback/Save',Staff_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

    path('Staff/Take_Attendance', Staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance', Staff_views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('Staff/View_Attendance', Staff_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),
    path('Staff/Attendance_Present/<str:id>',Staff_views.ATTENDANCE_PRESENT,name='attendance_present'),
    path('Staff/Attendance_Absent/<str:id>',Staff_views.ATTENDANCE_ABSENT,name='attendance_absent'),


    path('Staff/Add/Result', Staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('Staff/Save/Result', Staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),


    #this is STUDENT panel
    path('Student/Home', Student_views.HOME,name='student_home'),


    path('Student/Notification',Student_views.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),


    path('Student/Feedback',Student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/Feedback/Save',Student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

    path('Student/apply_for_leave',Student_views.STUDENT_LEAVE,name='student_leave'),
    path('Student/Leave_save',Student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),

    path('Student/View_Attendance',Student_views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),

    path('Student/View_Result',Student_views.VIEW_RESULT,name='view_result'),



]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
