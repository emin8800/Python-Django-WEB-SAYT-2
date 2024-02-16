from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.db.models import Q

from core.models import *
from core.forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

# def about(request):
#     return render (request, 'about.html')

def index2(request):
    return render (request, 'index2.html')

def becomeI(request):
    return render (request, 'become-instructor.html')

def pricing(request):
    return render (request, 'pricing.html')

# def faqs(request):
#     return render (request, 'faqs.html')

def faqs(request):
    faqs = FAQ.objects.all()
    context = {
        
        'faqs' : faqs,
        
    }
    return render(request, 'faqs.html', context)



def gallery(request):
    return render (request, 'gallery.html')



def course_list(request):
    return render (request, 'course-list.html')

def course_timeline(request):
    return render (request, 'course-timeline.html')

def instructors(request):
    return render(request, 'instructors.html')



def about(request):
    about = About.objects.all()
    context = {
        'about': about,
        'title': 'About',
    }
    return render(request, 'about.html', context)


def blog(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at') #updated_at
    context = {
        'blogs': blogs,
        'title': blogs
    }
    return render (request, 'blog.html', context)



def blog_details(request, slug):
    context = {
        'blogs': Blog.objects.get(slug=slug)
    }
    return render(request, 'blog_details.html', context)





class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'
    paginate_by = 2

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['count'] = Blog.objects.filter(is_published=True).count()
        query = self.request.GET.get('blog')
        if query:
            context['blog'] = Blog.objects.filter(title__icontains=query)
        context['title'] = 'Blog'
        return context
        
       
    


        # context = super().get_context_data(**kwargs)
        # blog_title = self.request.GET.get('blog')
        # start_date = self.request.GET.get('startdate')
        # end_date = self.request.GET.get('enddate')
        # category = self.request.GET.get('cat')
        # context['categories'] = Category.objects.all()
        # context['blog'] = Blog.objects.filter(is_published=True).order_by('-updated_at')

        # if blog_title and (start_date or end_date) and category:
        #     context['blog'] = Blog.objects.filter(
        #         Q(title__icontains=blog_title) | Q(description__icontains=blog_title),
        #         created_at__range=[start_date, end_date], category__id=category
        #     )
        # elif blog_title:
        #     context['blog'] = Blog.objects.filter(Q(title__icontains=blog_title) | Q(description__icontains=blog_title))
        # elif start_date or end_date:
        #     context['blog'] = Blog.objects.filter(created_at__range=[start_date, end_date])
        # elif category:
        #     context['blog'] = Blog.objects.filter(category__id=category)
        # else:
        #     context['blog'] = Blog.objects.filter(is_published=True).order_by('-updated_at')

        # context['title'] = 'Blog'
        # context['count'] = Blog.objects.filter(is_published=True).count()

        # context['blog_title'] = blog_title
        # context['start_date'] = start_date
        # context['end_date'] = end_date
        # context['category'] = category
        # return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

def contact(request):
    context = {
        'title': 'Contact',
        'form': ContactForm(),
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponse('Thank yopu for your message')
    return render (request, 'contact.html', context)

            # context ['success'] = True
            # context['form'] = ContactForm()


# def set_language(request):
#     lang_code = request.GET.get('language')
#     response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     if lang_code in dict(settings.LANGUAGES).keys():
#         print("tfgvbhjnkm")
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
#     return response

def search(request):
    print("request get: ", request.GET)
    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(title__icontains=query)
        course = Course.objects.filter(title__icontains=query)
        context = {
            'title': 'Search',
            'query': query,
            'blogs': blogs,
            'course': course,
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))


# def courseGrid(request):
#     context = {
#         'title': 'Course Grid',
#         'CourseGrid': Product.objects.filter(is_published=True).order_by('-created_at')
    
#     }
#     return render (request, 'course-grid.html', context)

# def course_details(request, pk):
#     courses = Product.objects.filter(is_published=True).order_by('-created_at')
#     courses2 = Product.objects.filter(is_published=True).order_by('-created_at')
#     context = {
#          'CourseGrid': Product.objects.get(id=pk),
#          'courses': courses[:5],
#          'courses2': courses2[:4]
#     }

#     return render (request, 'course_details.html', context)





def shop(request):
    context = {
        'title': 'Shop',
        'Shop': Shop.objects.filter(is_published=True).order_by('-created_at')
    }
    return render(request, 'shop.html', context)



def product_details(request):
    return render (request, 'product-details.html')



def course(request):
    course = Course.objects.all()[:4]
   
    level = Level.objects.all()
    time = Time.objects.all()
    pricecat = Pricecat.objects.all()
    coursecategory = Coursecategory.objects.all()


    if "level" in request.GET.keys():
        print(request.GET["level"])
        course = Course.objects.filter(
            level_id__title=request.GET["level"])
         
   
        
    if "time" in request.GET.keys():
      
        course = Course.objects.filter(
            time_id__title=request.GET["time"]) 
        
    if "pricecat" in request.GET.keys():
      
        course = Course.objects.filter(
            pricecat_id__title=request.GET["pricecat"]) 

    if "coursecategory" in request.GET.keys():
        course = Course.objects.filter(
            coursecategory_id__title=request.GET["coursecategory"]) 


    count = 4
    if request.method == 'POST':
        more = int(request.POST['more-course'])
        course = Course.objects.all()[:more+2]
        count = len(course)
        
 
    context = {
        'course': course,
        'course1': course,   # blog.html 166 setr 
        'level' : level,
        'time': time,
        'count': count,
        'pricecat': pricecat,
        'coursecategory': coursecategory,
        'title': 'Course'

    }
    return render (request, 'course-grid.html', context)



def course_details(request, slug):
    context = {
        'course': Course.objects.get(slug=slug)
    }
    return render(request, 'course_details.html', context)
