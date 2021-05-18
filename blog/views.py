from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_home(request):
   blog_lists = Blog.objects.all()
   return render(request, 'blog/blog_home.html', {'blog_lists': blog_lists})


def detail(request, blog_detail_id):
   blog_id = get_object_or_404(Blog, pk=blog_detail_id)
   return render(request, 'blog/detail.html', {'blog_id': blog_id})




# this is for search bar for search item.

def list_detail(request):

   if request.method == "POST":
      searched = request.POST['search']
      
      if searched =='':
         return render(request, 'blog/list_detail.html')
      else:
         results = Blog.objects.all().filter(title__contains=searched)
   
         return render(request, 'blog/list_detail.html', {"detail_lists": results})
   else:
      #submitted = False
      return render(request, 'blog/list_detail.html')

      #title was variable from Blog database(my own database)
      #__contains was parameters from sql_lite command line python.

   #detial_lists = Blog.objects.all()
      #return render(request, 'blog/list_detail.html', {"detail_lists": results})







# def search(request):
#    if request.method == "POST":
#       searched = request.POST['search']
#       results = Blog.objects.filter(name__contains=searched)
      
#       return render(request, 'blog/review.html', {'searched': searched}, {'results':results})

