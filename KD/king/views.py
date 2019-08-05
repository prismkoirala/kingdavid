from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#for_DBmodels
from king.models import ProductID, ProductPage, Customers,UserProfileInfo

from . import forms
from king.forms import NewUser, UserForm, UserProfileInfoForm
#for_paginator
from django.core.paginator import Paginator
#for_login
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def header(request):
    return render(request,'king/header.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('king:index'))

@login_required
def special(request):
    return HttpResponse("YOURE LOGGED IN")

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    dic = {'user_form' : user_form,'profile_form' : profile_form,'registered' : registered}

    return render(request,'king/registration.html',context=dic)


def product_page(request, product_name_slug ):

    product_info = ProductPage.objects.get(slug=product_name_slug)

    dic = {'page_info' : product_info, 'product_name' : product_info.p_title,
        'product_price' : product_info.p_price, 'description_short' : product_info.description_short,
        'p_description_long1' : product_info.p_description_long1,'image' : product_info.image,
        'p_description_long2' : product_info.p_price,
        'image2' : product_info.image2,'p_img' : product_info.p_img
        }

    return render(request,'king/product_page.html',context=dic)

def product_list(request):
    display = ProductPage.objects.order_by('id')

    paginator = Paginator(display, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    dic = { 'list': queryset }
    return render(request,'king/product_list.html',context=dic)

def index(request):
    display = ProductID.objects.order_by('id')
    display_customer = Customers.objects.order_by('id')
    dic = {'ids' : display, 'head' : "PERFUME DE TOILLETE",'dis' : display_customer}
    return render(request,'king/index.html',context=dic)



def form_view(request):
    form = NewUser()
    my_dict = {'form' : form }
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
        return index(request)
    else:
        print("Form invalid!")

    return render(request,'king/user_login_d.html',context=my_dict)
# Create your views here.
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('king:index'))
            else:
                return HttpResponse("account not active!")
        else:
            print("Incorrect username or password!")
            return HttpResponse("Invalid login details")
    else:
        return render(request,'king/login.html',{})
