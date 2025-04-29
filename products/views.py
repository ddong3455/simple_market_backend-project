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

# products/views.py

class ProductConfirmView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, id):
        product = get_object_or_404(Product, id=id)

        # 구매자가 본인인지 확인
        if product.buyer != request.user:
            return Response({'error': '구매 예약자가 아닙니다.'}, status=status.HTTP_403_FORBIDDEN)

        # 이미 판매 완료되었으면
        if product.status == '판매완료':
            return Response({'error': '이미 판매 완료된 상품입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # 상태를 판매완료로 변경
        product.status = '판매완료'
        product.save()

        return Response({'message': '구매가 확정되었습니다.'}, status=status.HTTP_200_OK)

# products/views.py

class MyPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        my_products = Product.objects.filter(seller=user)
        reserved_products = Product.objects.filter(buyer=user)

        my_data = ProductSerializer(my_products, many=True).data
        reserved_data = ProductSerializer(reserved_products, many=True).data

        return Response({
            "my_products": my_data,
            "reserved_products": reserved_data
        })
