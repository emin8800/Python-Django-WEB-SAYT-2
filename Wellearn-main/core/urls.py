from django.urls import path

from core.views import * 


urlpatterns = [
    path('', home ,  name='home'),

    path('about/', about, name='about' ),

    # path('blog_details/', blog_details, name='blog_details'),

    path('blog', BlogListView.as_view(), name='blog'),
    
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_details'),

    path('contact/', contact, name='contact'),


    path('index2/', index2, name='index2' ),

    path('become-instructor/', becomeI, name='become-instructor'),

    path('pricing/', pricing, name='pricing'),

    path('faqs/', faqs, name='faqs'),

    path('gallery/', gallery, name='gallery'),

    # path('course-grid/', courseGrid, name='course-grid'),

    path('course-list/', course_list, name='course-list'),
    path('course/', course, name='course-grid'),
    path('course/<slug:slug>/', course_details, name='course_details'),

    # path('course-grid/<int:pk>/', course_details, name='course_details'),

    path('course-timeline/', course_timeline, name='course-timeline'),

    path('instructors/', instructors, name='instructors'),

    path('search/', search, name='search'),

    path('shop/', shop, name='shop'),

    path('product-details', product_details, name='product-details'),

    
]