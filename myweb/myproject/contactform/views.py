from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def contact_add(request):
     

    if request.method == 'POST' or None :
        name = request.POST.get("name")
        email = request.POST.get("email")
        txt = request.POST.get("msg")

        if name == "" or email == "" or txt == "" :
            msg = "All Field are Requirded"
            return render(request, 'front/msgbox.html',{'msg':msg})
        try:
            b = ContactForm(cname=name,cemail=email,ctxt=txt) 
            b.save()
        except  :
            pass
        
        
        msg = "Your Message Receved"
        return render(request, 'front/msgbox.html',{'msg':msg})


    return render(request, 'front/msgbox.html')

def contact_show(request):
    #login check start.
    if not request.user.is_authenticated :
        return redirect('mylogin')
    #login check end.

    msg = ContactForm.objects.all()
    return render(request, 'back/contact_form.html',{'msg':msg})
