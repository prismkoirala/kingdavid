from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    phone_number = models.IntegerField(default='')

    profile_picture = models.ImageField(upload_to='profile_pics/', default='default/def.png')

    address = models.TextField(default="")

    def __str__(self):
        return self.user.username

class ProductID(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,blank=True,null=False)
    date = models.DateField()
    name = models.CharField(max_length=100,unique = True, default="")
    image = models.ImageField(upload_to = 'pro_img/', default='default/def.png', blank=True, null=True)
    def __str__(self):
        return self.name

class ProductPage(models.Model):
    p_id = models.ForeignKey(ProductID,on_delete=models.PROTECT, blank=True, null=True)
    p_title = models.CharField(max_length=100, unique = True)
    p_img = models.ImageField(upload_to = 'product_samples/%Y/%m/%d/',default="default/def.png")
    p_price = models.IntegerField(default="200")
    slug = models.SlugField(default="", unique=True)

    slides_img1 = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    slides_img2 = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    slides_img3 = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    slides_img4 = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    description_short = models.TextField(default='')

    image = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    p_description_long1 = models.TextField(default='')

    image2 = models.ImageField(upload_to = 'product_slides/',default="default/def_slides.jpg")
    p_description_long2 = models.TextField(default='')

    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                    #self.slug = slugify(self.name)
        self.slug = slugify(self.p_title)
        super(ProductPage, self).save(*args, **kwargs)


    def __str__(self):
        return self.p_title


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    readonly_fields=('id')
    user_name = models.CharField(max_length=55, unique = True)
    email = models.EmailField(unique = True)
    phone = models.IntegerField(unique = True)

    def __str__(self):
        return self.user_name

# Create your models here.
