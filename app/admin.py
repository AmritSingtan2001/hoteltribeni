from django.contrib import admin
from . models import SliderImages,AboutUs,Room,RoomRelatedImage,Gallery,\
    Testimonials,Blog,BlogCategory,Packages,FrequentlyAskedQuestion,Locality,Aminities


class SliderImageAdmin(admin.ModelAdmin):
    model:SliderImages
    list_display =['images']
admin.site.register(SliderImages,SliderImageAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    model: AboutUs
    list_display =['title','image1','image2']
admin.site.register(AboutUs, AboutUsAdmin)

class RoomRelatedImageAdmin(admin.TabularInline):
    model = RoomRelatedImage

class RoomAdmin(admin.ModelAdmin):
    inlines =[
        RoomRelatedImageAdmin
    ]
    list_display=['room_name','rate_per_night','size','capacity','bed','services']
admin.site.register(Room, RoomAdmin)

class GalleryAdmin(admin.ModelAdmin):
    model:Gallery
    list_display =['name','image']

admin.site.register(Gallery,GalleryAdmin)


class TestimonialsAdmin(admin.ModelAdmin):
    model:Testimonials
    list_display =['customer_name','image']
admin.site.register(Testimonials,TestimonialsAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    model:BlogCategory
    list_display =['category_name',]
admin.site.register(BlogCategory,BlogCategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    model:Blog
    list_display=['blog_title','blog_category','create_date','image']
admin.site.register(Blog,BlogAdmin)

class PackagesAdmin(admin.ModelAdmin):
    model:Packages
    list_display =['package_name','create_date','image','rate']
admin.site.register(Packages,PackagesAdmin)

class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    model:FrequentlyAskedQuestion
    list_display =['title','discriptions']
admin.site.register(FrequentlyAskedQuestion,FrequentlyAskedQuestionAdmin)


class LocalityAdmin(admin.ModelAdmin):
    model :Locality
    list_display = ['name','image','location']
admin.site.register(Locality,LocalityAdmin)



class AminitiesAdmin(admin.ModelAdmin):
    model:Aminities
    list_display =['aminities_name','image',]
admin.site.register(Aminities,AminitiesAdmin)