from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, Curriculum

# 목록 페이지
def index(request):
  subjects = Subject.objects.all()
  return render(request, 'subjects/index.html', {'subjects': subjects})

# 상세 페이지
def detail(request, id):
  subject = Subject.objects.get(id=id)
  curriculums = Curriculum.objects.filter(subject_id=id)
  return render(request, 'subjects/detail.html', {'subject': subject, 'curriculums': curriculums})

# 신청 페이지
def apply(request, id):
  subject = Subject.objects.get(id=id)
  return render(request, 'subjects/apply.html', {'subject': subject})