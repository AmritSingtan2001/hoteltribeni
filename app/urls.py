from django.urls import path
from . import views
from .views import RoomListViews,RoomDetailView,GalleryListView,BlogDetailView,\
    PackagesListView,PackageDetailsView,FAQListView,LocalityListView,LocalityDetailView,\
    AminitiesListView,AniminitiesDetailsView

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.aboutus, name="about"),
    path('rooms', RoomListViews.as_view(), name='rooms'),
    path('room/details/<slug:room_slug>',RoomDetailView.as_view(), name='room_details'),
    path('gallery', GalleryListView.as_view(), name='gallery_image'),
    path('blog/<slug:blog_slug>',BlogDetailView.as_view(), name='blogdeatils'),
    path('packages',PackagesListView.as_view(), name='package'),
    path('packages/<slug:package_slug>',PackageDetailsView.as_view(), name='package_details'),
    path('faq', FAQListView.as_view(), name='faq'),
    path('locality', LocalityListView.as_view(), name="locality"),
    path('contact', views.contact, name="contact"),
    path('locality/<slug:locality_slug>', LocalityDetailView.as_view(), name="localitydetail"),
    path('animinities', AminitiesListView.as_view(), name='animinities'),
    path('animinities/<slug:aminitie_slug>', AniminitiesDetailsView.as_view(), name='animinitiesdetails')
]