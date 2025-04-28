from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view()),  # ← 여기! signup 뒤에 '/' 슬래시 꼭 붙여야 해!!
]
from .views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),  # ★ 추가
]
