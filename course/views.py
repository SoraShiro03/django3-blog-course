from django.db.models.base import Model
from django.http import request
from django.shortcuts import render
from .models import Course



def home(request):
   course_lists = Course.objects.all()
   return render(request, 'course/home.html',{'course_lists': course_lists})


def what_news(request):
   return render(request, "course/whatnews.html")




# def search (request):
#     #defines what happens when there is a POST request
#     if request.method == "POST":
#         title = request.POST.get("search")
#         result = Blog.objects.all().filter(title)
#         return render(request,'course/search_result.html', { 'result' : result })


#     #defines what happens when there is a GET request
#     else:
#         return render(request,'course/searchpage.html')