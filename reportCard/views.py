from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .utils import send_email_to_client
# Create your views here.


def report(request):
  return render(request, 'reportCard/home.html')


def get_students(request):
  queryset = Student.objects.all()


# search function
  if request.GET.get('search'):
    search = request.GET.get('search')
    queryset = queryset.filter(
      Q(student_name__icontains = search) | 
      Q(department__department__icontains = search) | 
      Q(student_id__student_id__icontains = search) | 
      Q(student_email__icontains = search) | 
      Q(student_age__icontains = search) 
      
      )

# pagination
  paginator = Paginator(queryset, 10)
  page_num = request.GET.get("page", 1)
  page_obj = paginator.get_page(page_num)

  return render(request, 'reportCard/student.html', {'queryset':page_obj})


from .seed import generate_report_card
def see_marks(request, student_id):
  queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
  total_marks = queryset.aggregate(total_marks = Sum('marks'))


  return render(request, 'reportCard/see_marks.html', {'queryset': queryset, 'total_marks':total_marks})


def send_email(request):
  send_email_to_client()
  return redirect('/')