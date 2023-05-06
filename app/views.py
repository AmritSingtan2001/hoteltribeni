from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import SliderImages,AboutUs,Room,Testimonials,Gallery,Blog,\
    Packages,FrequentlyAskedQuestion,Locality,Aminities
from django.views.generic import ListView,DetailView

def index(request):
    sliderimage = SliderImages.objects.all()
    aboutus= AboutUs.objects.first()
    rooms = Room.objects.all()[:4]
    testimonials= Testimonials.objects.all()
    allblog = Blog.objects.all()[:5]
    return render(request,'app/index.html',{'slider_image':sliderimage,
                                            'aboutus':aboutus,
                                            'rooms':rooms,
                                            'testimonals':testimonials,
                                            'threeblog':allblog[:3],
                                            'blogs':allblog[3:]
                                            })


def aboutus(request):
    aboutus = AboutUs.objects.first()
    return render(request,'app/about-us.html',{'about':aboutus})


class RoomListViews(ListView):
    model= Room
    context_object_name='rooms'
    template_name ='app/rooms.html'

class RoomDetailView(DetailView):
    model = Room
    template_name ='app/room-details.html'
    slug_field = 'room_slug'
    slug_url_kwarg = 'room_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(RoomDetailView,self).get_context_data(*args, **kwargs)
        context["roomdetails"] = get_object_or_404(Room, room_slug=self.kwargs['room_slug']) 
        return context
    

class GalleryListView(ListView):
    model= Gallery
    context_object_name='gallery_images'
    template_name ='app/gallery.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name ='app/blog-details.html'
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView,self).get_context_data(*args, **kwargs)
        blog = get_object_or_404(Blog, blog_slug=self.kwargs['blog_slug'])
        context["blogdetails"] =  blog
        context['relatedblog'] = Blog.objects.filter(blog_category = blog.blog_category)[:3]
        return context
    

class PackagesListView(ListView):
    model  = Packages
    template_name = 'app/packages.html'
    context_object_name = 'packages'

class PackageDetailsView(DetailView):
    model = Packages
    template_name ='app/packagesdtails.html'
    slug_field = 'package_slug'
    slug_url_kwarg = 'package_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(PackageDetailsView,self).get_context_data(*args, **kwargs)
        context["packagedetails"] =  get_object_or_404(Packages, package_slug=self.kwargs['package_slug'])
        return context
    


class FAQListView(ListView):
    model=FrequentlyAskedQuestion
    template_name = 'app/faq.html'
    context_object_name ='faqs'


def contact(request):
    return render(request,'app/contact.html')


class LocalityListView(ListView):
    model = Locality
    template_name ='app/locality.html'
    context_object_name ='localities'

class LocalityDetailView(DetailView):
    model = Locality
    template_name ='app/localitydetails.html'
    slug_field = 'locality_slug'
    slug_url_kwarg = 'locality_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(LocalityDetailView,self).get_context_data(*args, **kwargs)
        context["localitydetail"] =  get_object_or_404(Locality, locality_slug=self.kwargs['locality_slug'])
        return context
    
class AminitiesListView(ListView):
    model = Aminities
    template_name ='app/anminities.html'
    context_object_name ='animinities'



class AniminitiesDetailsView(DetailView):
    model = Aminities
    template_name ='app/animinitiesdetails.html'
    slug_field = 'aminitie_slug'
    slug_url_kwarg = 'aminitie_slug'
    
    def get_context_data(self, *args, **kwargs):
        context = super(AniminitiesDetailsView,self).get_context_data(*args, **kwargs)
        context["animinitiesdetails"] =  get_object_or_404(Aminities, aminitie_slug=self.kwargs['aminitie_slug'])
        return context
    