


from django.shortcuts import render, redirect
from app.forms import BlogPostForm,CustomUserForm,AdminProfileForm,EmployeeProfileForm,ProfilePicUploadForm
from app.models import *
from django.contrib import messages
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, "index.html")
# def login_page(request):
#     return render(request,'login.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if (request.method=='POST'):
            usr=request.POST.get('username')
            pswd=request.POST.get('password')
            user = authenticate(request,username=usr,password=pswd)
            if user is not None:
                login(request, user)
                if user.role=="ADMIN":
                    messages.success(request,'Admin logged in successfully')
                    return redirect('adminhome')
                elif user.role=="EMPLOYEE":
                    messages.success(request,'Employee logged in successfully')
                    return redirect('emphome')
                elif user.role=="CUSTOMER":
                    messages.success(request,'Customer logged in successfully')
                    return redirect('cushome')
                else:
                    messages.success(request,'invalid user')
            else:
                messages.error(request,'invalid Login credentials')
        return render(request,'registration/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'user has been logged out')
    return redirect('login')

def admin_home(request):
    admins=AdminProfile.objects.all().order_by('-user_id')
    context={
        'data':admins
    }
    return render(request,'users/admin/admin_home.html',context)

def add_emp(request):
    if request.method == 'POST':
        form2=EmployeeProfileForm(request.POST, request.FILES)
        if form2.is_valid():
            # e1=Employee.objects.create_user(
            #     username=form2.cleaned_data.get('username'),
            #     email=form2.cleaned_data.get('email'),
            #     first_name=form2.cleaned_data.get('first_name'),
            #     last_name=form2.cleaned_data.get('last_name'),
            #     password=form2.cleaned_data.get('password1')
            # )
            e1=form2.save()
            print(e1,'form2 saved')
            user=EmployeeProfile.objects.get(pk=e1.id)
            user.emp_phon=form2.cleaned_data.get('emp_phone')
            user.emp_address=form2.cleaned_data.get('emp_address')
            user.profile_pic=request.FILES.get('profile_pic')
            user.save()
            messages.success(request,'Successfully added Employee')
            return redirect('manage_emp')
        else:
            # print('Form error : ',form.errors)
            print("Form 2 error : ",form2.errors)
            messages.error(request,'somthing went wrong')
            
    else:
        # form = CustomUserForm()
        form2 = EmployeeProfileForm()
        # form3 = AdminProfileForm()
    context={
            # 'data':form,
            'data2':form2,
              } #'data3':form3
    return render(request,'users/admin/add_emp.html',context)


def manage_emp(request):
    employees=Employee.objects.all()
    employeesdetails=EmployeeProfile.objects.all().order_by('-user_id')
    context={
        #'data1':employees,
        'data2':employeesdetails
    }
    return render(request,'users/admin/manage_emp.html',context)

# def upload_pic(request, form, user_id):
#         if request.method == 'POST':
#             if form.is_valid():
#                 Admin=get_user_model
#                 user = Admin.objects.get(user_id=user_id)
#                 profile_pic = form.cleaned_data.get('profile_pic')
#                 new_user_profile = AdminProfile.objects.create(user_id=user_id, profile_pic=profile_pic)
#                 new_user_profile.save()

def add_admin(request):
    if request.method == 'POST':
        form3=AdminProfileForm(request.POST)
        form=ProfilePicUploadForm(request.POST, request.FILES)
        if form3.is_valid() and form.is_valid():
            # username=form3.cleaned_data.get('username')
            # password=form3.cleaned_data.get('password1')
            # email=form3.cleaned_data.get('email')
            # e1=Admin.objects.create_user(username=username,password=password,email=email)
            a1=form3.save()
            # print(e1,'form3 saved')
            user=AdminProfile.objects.get(pk=a1.id)
            user.admin_phon=form3.cleaned_data.get('admin_phon')
            user.admin_address=form3.cleaned_data.get('admin_address')
            user.profile_pic=request.FILES.get('profile_pic')
            user.save()
            # print(user,'form saved')
            # upload_pic(request,ProfilePicUploadForm,user_id=e1.id)

            messages.success(request,'Successfully added Admin')
            return redirect('adminhome')
        else:
            # print('Form error : ',form.errors)
            # print("Form 3 error : ",form3.errors)
            messages.error(request,'Failed to add admin')
    else:
        form3 = AdminProfileForm()
        form=ProfilePicUploadForm()
    context={
        'data3':form3,
        'data4':form
         }
    return render(request,'users/admin/add_admin.html',context)


def employee_home(request):
    return render(request,'users/emp/emp_home.html')

def customer_home(request):
    return render(request,'users/custmr/cus_home.html')

def blog(request):
    myform=BlogPostForm()
    if request.method=='GET':
        post=Blog.objects.all().order_by('-id')
        context={
            'data':post,
            'data2':myform
        }
        return render(request, "blog.html",context)


def blog_post(request):
    if request.method=='POST':
        myform=BlogPostForm(request.POST,request.FILES)
        if myform.is_valid():
            b1=Blog.objects.create(
                                    title=myform.cleaned_data.get('title'),
                                    old_pic=request.FILES.get('old_pic'),
                                    current_pic=request.FILES.get('current_pic'),
                                    updates=myform.cleaned_data.get('updates'),
                                    posted_by=request.user
                                    )
            b1.save()
            messages.success(request,'Your blog posted successfully')
            return redirect ('blog')
        else:
            print(myform.errors)
            print("error")
            messages.error(request,'Somthing went wrong!')
            return redirect('blog')


def contact_us(request):

    return render(request, "contactus.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def login_admin(request):
    return redirect("/admin/")
