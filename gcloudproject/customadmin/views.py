from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import *
from loginapp.models import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, InvalidPage



# Create your views here.

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('customadmin:adminhome')
            else:
                messages.info(request,"only admins can login")
        else:
            messages.info(request, 'Invalid Details')
            return redirect('customadmin:adminlogin')
    return render(request, "cuadmin/signin.html")

def adminLogout(request):
    auth.logout(request)
    return redirect('mainapp:home')

def adminHome(request):
    contact = Contact.objects.all()
    paginator = Paginator(contact, 4)
    try:
        page = int(request.GET.get('page', "1"))
    except:
        page = 1
    try:
        contact = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contact = paginator.page(paginator.num_pages)

    user = CustomUser.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('customadmin:adminhome')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('customadmin:adminhome')
            else:
                user = CustomUser.objects.create_user(username=username, password=password1, email=email,phone=phone)
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.save();
        else:
            messages.info(request, 'Password not matched')
            return redirect('customadmin:adminhome')
        return redirect('customadmin:adminhome')
    return render(request,'cuadmin/index.html',{'user':user,'contact':contact})

def deleteMessage(request,id):
    msg = Contact.objects.get(id=id)
    if request.method == 'POST':
        msg.delete()
        return redirect('customadmin:adminhome')
    # return render(request,'cuadmin/index.html')
    

# def adminWidget(request):
#     orders = Orders.objects.filter()
#     f_orders = PaymentFailed.objects.all()
#     s_orders = PaymentSuccess.objects.all()
#     return render(request,"cuadmin/widget.html",{'orders':orders,"f_orders":f_orders,"s_orders":s_orders})

def adminWidget(request):
    orders = Orders.objects.filter()
    f_orders = PaymentFailed.objects.all()
    s_orders = PaymentSuccess.objects.all()
    return render(request, "cuadmin/widget.html", {'orders': orders, "f_orders": f_orders, "s_orders": s_orders})


def adminProfile(request):
    users = CustomUser.objects.filter(is_verified=True)
    search = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        search = CustomUser.objects.filter(Q(name__contains=query) | Q(phone__contains=query))
    return render(request,"cuadmin/adminprofile.html",{'users':users,'search':search,'query':query})

def adminTable(request):
    normal_type = TemplatesType.objects.get(name='normal')
    normal = Templates.objects.filter(temp_type=normal_type)
    search = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        search = normal.filter(Q(name__contains=query) | Q(category__contains=query))
    return render(request,"cuadmin/normaltable.html",{'normal': normal, 'query': query, 'search': search})

# def delete_normal_temp(request, normal_id):
#     normal = Templates.objects.get(id=normal_id)
#     if request.method == 'POST':
#         normal.delete()
#         return redirect('customadmin:admintable')
#     return render(request, 'cuadmin/normaltable.html')


import os
import shutil
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect

def delete_normal_temp(request, normal_id):
    try:
        normal = Templates.objects.get(id=normal_id)
    except Templates.DoesNotExist:
        return HttpResponse("Template not found", status=404)

    if request.method == 'POST':
        # Get the paths to the zip file and extracted folder
        zip_file_path = normal.temp_file.path
        extracted_dir = os.path.join(settings.MEDIA_ROOT, "templates", os.path.splitext(os.path.basename(zip_file_path))[0])

        # Delete the Template object from the database
        normal.delete()

        # Delete the zip file
        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)

        # Delete the extracted folder
        if os.path.exists(extracted_dir):
            shutil.rmtree(extracted_dir)

        # Delete template images using Django FileField methods
        if normal.temp_img:
            image_path = normal.temp_img.path
            print(f"Image Path: {image_path}")  # For debugging
            default_storage.delete(image_path)

        return redirect('customadmin:admintable')

    return render(request, 'cuadmin/normaltable.html')


def update_normal(request, card_id):
    # Templates = get_object_or_404(Templates, id=card_id)
    if request.method == 'POST':
        category = request.POST['category']
        type = request.POST['type']
        # price = request.POST['price']
        temp_type = TemplatesType.objects.get(name=type)
        if temp_type == 'normal':
            n = 199
        else:
            n = 399
        Templates.objects.filter(id=card_id).update(category=category,temp_type=temp_type,price=n)
        return redirect('customadmin:admintable')

def adminTableP(request):
    premium_type = TemplatesType.objects.get(name='premium')
    premium = Templates.objects.all().filter(temp_type=premium_type)
    search = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        search = premium.filter(Q(name__contains=query) | Q(category__contains=query))
    return render(request,'cuadmin/premiumtable.html',{'premium':premium, 'query': query, 'search': search})

def delete_premium_temp(request, premium_id):
    premium = Templates.objects.get(id=premium_id)
    if request.method == 'POST':
        premium.delete()
        return redirect('customadmin:admintablep')
    return render(request, 'cuadmin/premiumtable.html')

def update_premium(request, card_id):
    # Templates = get_object_or_404(Templates, id=card_id)
    if request.method == 'POST':
        category = request.POST['category']
        type = request.POST['type']
        # price = request.POST['price']
        temp_type = TemplatesType.objects.get(name=type)
        if temp_type == 'premium':
            n = 399
        else:
            n = 199
        Templates.objects.filter(id=card_id).update(category=category,temp_type=temp_type,price=n)
        return redirect('customadmin:admintablep')

def adminForm(request):
    normal = TemplatesType.objects.all()
    if request.method == 'POST':
        temp_img = request.FILES.get('temp_img')
        temp_file = request.FILES.get('temp_file')
        name = request.POST['name']
        find = request.POST['find']
        category = request.POST['category']
        temp_type_normal = request.POST['temp_type']
        price = request.POST['price']
        temp_type = TemplatesType.objects.get(name=temp_type_normal)
        card = Templates(temp_img=temp_img,temp_file=temp_file,name=name,find=find,temp_type=temp_type,price=price,category=category)
        card.save()
        return redirect('customadmin:admintable')
    return render(request,"cuadmin/normalform.html",{'normal':normal})

def adminFormP(request):
    if request.method == 'POST':
        temp_img = request.FILES.get('temp_img')
        temp_file = request.FILES.get('temp_file')
        name = request.POST['name']
        find = request.POST['find']
        category = request.POST['category']
        temp_type_premium = request.POST['temp_type']
        price = request.POST['price']
        temp_type = TemplatesType.objects.get(name=temp_type_premium)
        card = Templates(temp_img=temp_img, temp_file=temp_file, name=name, find=find,temp_type=temp_type, price=price,category=category)
        card.save()
        return redirect('customadmin:admintablep')
    return render(request,"cuadmin/premiumform.html")

# def adminCoupenTable(request):
#     show_coupen = Coupen_code.objects.all()
#     return render(request,'cuadmin/coupen.html',{'show_coupen':show_coupen})

def adminCoupen(request):
    show_coupen = Coupen_code.objects.all()
    if request.method == 'POST':
        code = request.POST['code']
        coupen_percentage = request.POST['coupen_percentage']
        orders = Coupen_code(code=code,coupen_percentage=coupen_percentage,created_date=timezone.now())
        orders.save()
        return redirect('customadmin:admincoupen')
    return render(request,'cuadmin/coupen.html',{'show_coupen':show_coupen})

def deleteCoupen(request,c_id):
    del_coupen = Coupen_code.objects.get(id=c_id)
    # del_coupen = get_object_or_404(Coupen_code, id=c_id)
    if request.method == 'POST':
        del_coupen.delete()
        return redirect('customadmin:admincoupen')
    return render(request, 'cuadmin/coupen.html')

