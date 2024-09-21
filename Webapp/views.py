from django.shortcuts import render,redirect
from Webapp.models import contactDB,registerDB
from Backend.models import categoryDB,productDB
from django.contrib import messages


# Create your views here.
def home_page(req):
    cat_det=categoryDB.objects.all()
    return render(req,"home.html",{'cat_key':cat_det})

def about_page(req):
    return render(req,"about.html")

def contact_page(req):
    return render(req,"contact.html")

def save_contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msge=request.POST.get('msge')
        obj=contactDB(name=name,email=email,message=msge)
        obj.save()
        messages.success(request, "Message sent successfully...")
        return redirect(contact_page)

def category_page(request,category_name):
    cat_det=categoryDB.objects.get(category_name=category_name)
    pro_det=productDB.objects.filter(category_name=category_name)
    return render(request, "category.html", {'pro_key': pro_det, 'cat_key': cat_det})

def product_page(request):
    pro_det=productDB.objects.all()
    return render(request,"product.html",{'pro_key':pro_det})

def main_register_page(request):
    return render(request,"login.html")

def login_page(request):
    from Backend.views import admin_login
    return redirect(admin_login)

def save_reg(request):
    if request.method == "POST":
        name=request.POST.get('uname')
        email=request.POST.get('email')
        passw=request.POST.get('pass')
        if registerDB.objects.filter(username=name).exists():
            return redirect(main_register_page)
        elif registerDB.objects.filter(email=email).exists():
            return redirect(main_register_page)
        else:
            sav=registerDB(username=name,email=email,password=passw)
            sav.save()
            return redirect(main_register_page)

def payment_page(requst):
    return render(requst,'payment.html')
