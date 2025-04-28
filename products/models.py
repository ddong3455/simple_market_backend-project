from django.db import models
from users.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='판매중')
    created_at = models.DateTimeField(auto_now_add=True)

# models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = [
        ('판매중', '판매중'),
        ('예약중', '예약중'),
        ('판매완료', '판매완료'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='판매중')
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchases')  # ★ 추가

    def __str__(self):
        return self.title
