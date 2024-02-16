from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True




class Blog(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    description = RichTextField(blank=True, null=True, help_text='for the data')
    image = models.ImageField(upload_to='media/news')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True,)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')

    def get_absolute_url(self):
        return f'/blog/{self.slug}'
    

    def save(self, *args,**kwargs):
        from core.utils.mixis import custom_slugify
        self.slug = custom_slugify(self.title)
        
        super(Blog, self).save(*args, **kwargs)
            


class Category(BaseModel):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'




class Settings(BaseModel):
    logo = models.ImageField(upload_to='media/settings')
    number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    youtube = models.URLField()

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return 'Saytın Funksiyaları'
    
class Contact(BaseModel):
    Fname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.Fname
    
    class Meta:
        verbose_name_plural = 'Contacts'

class test(BaseModel):
    title = models.CharField(max_length=200)


#pip install django-phone-field
# from django.db import models
# from phone_field import PhoneField

# class MyModel(models.Model):
#     name = models.CharField(max_length=128)
#     phone = PhoneField(blank=True, help_text='Contact phone number')


class About(BaseModel):
    title = models.CharField(max_length=200) 
    description = RichTextField(blank=True, null=True, help_text='for the data')
    image = models.ImageField(upload_to='media/about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')


class Subscriber(BaseModel):
    # name = models.CharField(max_length=25)
    email = models.EmailField()
    # message = models.TextField()
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
    class Meta:
       verbose_name = 'Subscribers'
       verbose_name_plural = 'Subscribers'


class ProductCategory(BaseModel):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Category'



class Product(BaseModel):
    title = models.CharField(max_length=50)
    title_two = models.CharField(max_length=150)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = 'Products'


class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket')
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title      
    


class ShopCategory(BaseModel):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Shop Category'
        verbose_name_plural = 'Shop Category'


class Shop(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Shops')
        verbose_name_plural = 'Shops'

    
class Level(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title

class Price(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title
    

class Time(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title  

class Pricecat(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title  

class Coursecategory(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title
    

class Course(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    title_two = models.CharField(max_length=150)
    Q = models.CharField(max_length=150)

    description = models.TextField()
    image = models.ImageField(upload_to='media/news')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True,)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    pricecat = models.ForeignKey(Pricecat, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    coursecategory = models.ForeignKey(Coursecategory, on_delete=models.CASCADE)
    
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Course')

    def get_absolute_url(self):
        return f'/course/{self.slug}'
    

    def save(self, *args,**kwargs):
        from core.utils.mixis import custom_slugify
        self.slug = custom_slugify(self.title)
        
        super(Course, self).save(*args, **kwargs)



class FAQ(BaseModel):
    question = RichTextField(max_length=300, verbose_name=("Sual"))
    answer = RichTextField(max_length=10000, verbose_name=("Cavab"))
    order = models.IntegerField(default=0, verbose_name=("Sıra"))

    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        ordering = ("order",)