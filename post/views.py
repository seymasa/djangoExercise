from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Post

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts}) # -->'post' = template te kullanacagımız, posts ise yukarıda oluşturdugum değişken...

def post_detail(request):
    return HttpResponse('Burası Post Detail i')

def post_create(request):
    return HttpResponse('Burası Post Create i')

def post_update(request):
    return HttpResponse('Burası Post Update i')

def post_delete(request):
    return HttpResponse('Burası Post Delete i')



