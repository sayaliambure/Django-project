from django.urls import path
from reportCard import views


urlpatterns = [
  path('', views.report, name = "report"),
  path('/send_email', views.send_email, name = "send_email"),
  path('student/', views.get_students, name = "student"),
  path('marks/<student_id>/', views.see_marks, name = "marks"),


]