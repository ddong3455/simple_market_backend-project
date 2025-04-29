from django.urls import path
from .views import ProductCreateView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
]
from .views import ProductCreateView, ProductListView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),   # ★ 추가
]
from .views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:id>/', ProductDetailView.as_view()),   # ★ 추가
]

from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:id>/', ProductDetailView.as_view()),
    path('<int:id>/update/', ProductUpdateView.as_view()),   # ★ 추가
]

from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:id>/', ProductDetailView.as_view()),
    path('<int:id>/update/', ProductUpdateView.as_view()),
    path('<int:id>/delete/', ProductDeleteView.as_view()),  # ★ 추가
]

from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductReserveView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:id>/', ProductDetailView.as_view()),
    path('<int:id>/update/', ProductUpdateView.as_view()),
    path('<int:id>/delete/', ProductDeleteView.as_view()),
    path('<int:id>/reserve/', ProductReserveView.as_view()),  # ★ 추가
]

# products/urls.py

from .views import (
    ProductCreateView, ProductListView, ProductDetailView,
    ProductUpdateView, ProductDeleteView, ProductReserveView, ProductConfirmView
)

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('<int:id>/', ProductDetailView.as_view()),
    path('<int:id>/update/', ProductUpdateView.as_view()),
    path('<int:id>/delete/', ProductDeleteView.as_view()),
    path('<int:id>/reserve/', ProductReserveView.as_view()),
    path('<int:id>/confirm/', ProductConfirmView.as_view()),   # 🔥 추가
]

# products/urls.py

from .views import MyPageView  # ← 꼭 import 추가

urlpatterns = [
    # 기존 path들 ...
    path('mypage/', MyPageView.as_view()),  # 🔥 추가
]
