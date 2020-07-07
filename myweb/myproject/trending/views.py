from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout

def trending_add(request):

    if request.method == 'POST' or None:
        txt = request.POST.get('txt')

        if txt == "":
            error = "All Field are Requirded"
            return render(request, 'back/error.html',{'error':error})

        try:
            b = Trending(txt=txt)
            b.save()
        except:
            print("error")

    return render(request, 'back/trending.html')
 