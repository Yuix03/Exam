from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# Create your views here.
from django.views import View



from maqolaapp.models import Blog

from userapp.models import Muallif


class BlogView(View):
    def get(self, request):
        acc=Muallif.objects.get(user=request.user)
        if request.user.is_authenticated:
            data = {
                'blog': Blog.objects.filter(user=acc)
            }
            return render(request, 'Blog.html', data)
        else:
            return redirect('/login/')

class BlogidView(View):
    def get(self, request, a):
        b=Blog.objects.get(id=a)

        data =  {
              'uuu': b
        }
        return render(request,'Blogid.html',data)

