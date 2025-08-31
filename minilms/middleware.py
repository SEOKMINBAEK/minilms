# middleware.py (또는 utils/middleware.py)
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    # 로그인이 필요하지 않은 경로들
    exempt_urls = [
      reverse('login'),
      '/admin/login/',  # admin 로그인 페이지
      '/uploads/',        # 미디어 파일
    ]
      
    # 현재 경로가 예외 경로인지 확인
    path = request.path_info
    if not any(path.startswith(url) for url in exempt_urls):
      if not request.user.is_authenticated:
        return redirect('login')
      
    response = self.get_response(request)
    return response