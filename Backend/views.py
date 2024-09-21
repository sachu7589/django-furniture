from django.shortcuts import render, redirect
from Backend.models import categoryDB,productDB
from Webapp.models import contactDB,registerDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Webapp.views import home_page

# Create your views here.
def index_page(request):
    if 'uname' in request.session:
        return render(request,"index.html")
    else:
        return redirect(admin_login)

def add_category_page(req):
    return render(req,"add_category.html")

def save_category(request):
    if request.method == "POST":
        name=request.POST.get('cname')
        desc=request.POST.get('cdesc')
        img=request.FILES['cimage']
        obj=categoryDB(category_name=name,Description=desc,category_image=img)
        obj.save()
        messages.success(request,"Category added successfully..")
        return redirect(category_details)

def category_details(request):
    cat_det=categoryDB.objects.all()
    return render(request, "category_details.html",{'cat_key':cat_det})

def edit_category_page(request,cat_id):
    cat_det=categoryDB.objects.get(id=cat_id)
    return render(request,"edit_category.html",{'cat_key':cat_det})

def update_category(request, cat_id):
    if request.method == "POST":
        cat_name=request.POST.get('cname')
        cat_desc=request.POST.get('cdesc')
        try:
            img=request.FILES['cimage']
            fs=FileSystemStorage()
            img_file=fs.save(img.name,img)
        except MultiValueDictKeyError :
            img_file=categoryDB.objects.get(id=cat_id).category_image
        categoryDB.objects.filter(id=cat_id).update(category_name=cat_name,Description=cat_desc,category_image=img_file)
        return redirect(category_details)

def add_product(request):
    cat_det = categoryDB.objects.values('id', 'category_name')
    return render(request,"add_product.html",{'cat_key':cat_det})

def save_product(request):
    if request.method == "POST":
        pname=request.POST.get('pname')
        cname=request.POST.get('cname')
        desc=request.POST.get('pdesc')
        price=request.POST.get('pprice')
        img=request.FILES['pimage']
        obj= productDB(category_name=cname,Description=desc,product_name=pname,product_price=price,product_image=img)
        obj.save()
        return redirect(index_page)

def product_details(request):
    pro_data= productDB.objects.all()
    return render(request,"product_details.html",{'pro_key':pro_data})

def edit_product(request,pro_id):
    pro_det=productDB.objects.get(id=pro_id)
    cat_det=categoryDB.objects.values('category_name')
    return render(request, "edit_product.html",{'pro_key':pro_det,'cat_key':cat_det})

def admin_login(request):
    if 'uname' in request.session:
        return redirect(index_page)
    else:
        return render(request, "admin_login.html")

def load_backend_auth(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        ps = request.POST.get('pass')
        if registerDB.objects.filter(username=un, password=ps).exists():
            request.session['uname'] = un
            from Webapp.views import home_page
            return redirect(home_page)
        else:
            if User.objects.filter(username__contains=un).exists():
                x = authenticate(username=un, password=ps)
                if x is not None :
                    login(request, x)
                    request.session['uname']=un
                    return redirect(index_page)
                else:
                    return redirect(admin_login)
            else:
                return redirect(index_page)
    else:
        return redirect(index_page)

def admin_logout(request):
    del request.session['uname']
    return redirect(home_page)

def contact_details(request):
    con_det = contactDB.objects.all()
    return render(request,"contact_det.html",{'con_key':con_det})

def register_page(request):
    from Webapp.views import main_register_page
    return redirect(main_register_page)