from django.db import models
from base.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def __str__(self):
        return self.category_name
    
class ColorVarient(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name
    
class SizeVarient(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size_name
    


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    color_varient = models.ManyToManyField(ColorVarient, null=True, blank=True)
    size_varient = models.ManyToManyField(SizeVarient, null=True, blank=True)

    def __str__(self) -> str:
        return self.product_name

    def get_product_price_by_size(self, size):
        return self.price + SizeVarient.objects.get(size_name=size).price  




class ProductImage(BaseModel):
    product_image = models.ImageField(upload_to="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")



class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=10)
    is_valide = models.BooleanField(default=True)
    discounted_price = models.IntegerField(default=100)
    minimum_price = models.IntegerField(default=500)

