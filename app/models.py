from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


class SliderImages(models.Model):
    images = models.ImageField(upload_to='sliderimage/')



class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    discriptions = RichTextField()
    image1 = models.ImageField(upload_to='aboutimage/')
    image2 = models.ImageField(upload_to='aboutimage/')
    slug = AutoSlugField(populate_from= 'title', unique=True, null=True, default=None)
   
    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.title


class Room(models.Model):
    room_name = models.CharField(max_length=150)
    rate_per_night = models.PositiveIntegerField()
    size = models.CharField(max_length=150)
    capacity = models.CharField(max_length=150)
    bed = models.CharField(max_length=150)
    services = RichTextField()
    image = models.ImageField(upload_to='roomimages/')
    discriptions = RichTextField()
    room_slug = AutoSlugField(populate_from='room_name', unique=True, null=True, default=None)

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.room_name

    

class Testimonials(models.Model):
    customer_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='testimonials/', null=True,blank=True)
    discriptions = RichTextField()

    class Meta:
        ordering = ['-id',]
        verbose_name ="Testimonial"
        verbose_name_plural ="Testimonials"

    def __str__(self):
        return self.customer_name


    

class RoomRelatedImage(models.Model):
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_details')
    image = models.ImageField(upload_to='roomimages/')

    class Meta:
        ordering =['-id',]



class Gallery(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='galleryimages/')

    class Meta:
        ordering =['-id',]

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=150)
    category_slug = AutoSlugField(populate_from= 'category_name', unique=True, null=True, default=None)

    class Meta:
        ordering =['id']
    
    def __str__(self):
        return self.category_name


    
class Blog(models.Model):
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category') 
    blog_title = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogimages/')
    discriptions=RichTextField()
    blog_slug = AutoSlugField(populate_from='blog_title', unique=True, null=True, default=None)

    class Meta:
        ordering =['-id',]
        verbose_name ="Blog"
        verbose_name_plural ="Blogs"
    def __str__(self):
        return self.blog_title


class Packages(models.Model):
    package_name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='packageimages/')
    location = models.CharField(max_length=150)
    rate = models.PositiveIntegerField()
    discriptions=RichTextField()
    package_slug = AutoSlugField(populate_from='package_name', unique=True, null=True, default=None)

    class Meta:
        ordering =['-id',]
        verbose_name ="Package"
        verbose_name_plural ="Packages"

    def __str__(self):
        return self.package_name



class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=250)
    discriptions = RichTextField()

    class Meta:
        ordering =['id',]
        verbose_name ="Frequently Asked Question"
        verbose_name_plural ="Frequently Asked Questions"

    def __str__(self):
        return self.title
    

class Locality(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='localityimage/')
    location = models.CharField(max_length=150)
    discriptions = RichTextField()
    locality_slug = AutoSlugField(populate_from='name', null=True, unique=True, default=None)


    class Meta:
        ordering =['-id',]
        verbose_name ="Locality"
        verbose_name_plural ="Localities"
    
    def __str__(self):
        return self.name
    
class Aminities(models.Model):
    aminities_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='aminitiesimage/')
    discriptions = RichTextField()
    aminitie_slug = AutoSlugField(populate_from='aminities_name', null=True, unique=True, default=None)


    class Meta:
        ordering =['-id',]
        verbose_name ="Aminities"
        verbose_name_plural ="Aminities"

    
    def __str__(self):
        return self.aminities_name
    
