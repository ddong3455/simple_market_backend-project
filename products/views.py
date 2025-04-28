from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ProductSerializer

class ProductCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 로그인한 사람만 접근 가능

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)  # 현재 로그인한 사용자 정보를 seller로 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.seller:
            raise PermissionDenied('You do not have permission to edit this product.')
        serializer.save()

from rest_framework.exceptions import PermissionDenied

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.seller:
            raise PermissionDenied('You do not have permission to delete this product.')
        instance.delete()

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProductReserveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, id):
        product = get_object_or_404(Product, id=id)
        if product.status != '판매중':
            return Response({'error': '이미 예약중이거나 판매완료된 상품입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        product.status = '예약중'
        product.buyer = request.user
        product.save()
        
        return Response({'message': '상품이 예약되었습니다.'}, status=status.HTTP_200_OK)
