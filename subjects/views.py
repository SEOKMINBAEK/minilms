from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Subject, Curriculum, Apply
from .serializers import ApplySerializer
from rest_framework import viewsets

# 목록 페이지(/)
def index(request):
  subjects = Subject.objects.all()
  return render(request, 'subjects/index.html', {'subjects': subjects})

# 상세 페이지(/:id)
def detail(request, id):
  subject = Subject.objects.get(id=id)
  curriculums = Curriculum.objects.filter(subject_id=id)
  return render(request, 'subjects/detail.html', {'subject': subject, 'curriculums': curriculums})

# 신청 페이지(/apply/:id)
def apply(request, id):
  if request.method == 'GET':
    subject = Subject.objects.get(id=id)
    return render(request, 'subjects/apply.html', {'subject': subject})
  
  # 신청 처리
  elif request.method == 'POST':
    subject = Subject.objects.get(id=request.POST.get("subject_id"))
    subject_title = request.POST.get('subject_title')
    region = request.POST.get('region')
    frequency_type = request.POST.get('frequency_type')
    frequency_count = request.POST.get('frequency_count')
    class_count = request.POST.get('class_count')
    name = request.POST.get('name')
    email_id = request.POST.get('email_id')
    email_domain = request.POST.get('email_domain')
    direct_domain = request.POST.get('direct_domain')
    phone1 = request.POST.get('phone1')
    phone2 = request.POST.get('phone2')
    phone3 = request.POST.get('phone3')

    email = email_id + "@" + email_domain if email_domain != "direct" else direct_domain
    phone = phone1 + "-" + phone2 + "-" + phone3

    Apply.objects.create(
        subject=subject,
        subject_title=subject_title,
        region=region,
        frequency_type=frequency_type,
        frequency_count=frequency_count,
        class_count=class_count,
        name=name,
        email=email,
        phone=phone
    )
    
    send_mail(
        f'[{subject_title}] 수업 신청이 완료되었습니다.',
        f'''
        안녕하세요 {name}님.
        {subject_title} 수업 신청이 완료되었습니다.
        신청 내역은 담당자가 확인 후,
        {phone} 번호로 연락드리겠습니다.

        감사합니다.
        ''',
        'gatsby3130@gmail.com',
        [email, 'gatsby3130@gmail.com'],
        fail_silently=False,
    )

    return redirect('subjects:index')

def history(request):
    return render(request, 'subjects/history.html')

class ApplyViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer