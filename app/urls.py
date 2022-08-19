from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("blog", views.blog, name="blog"),
    # path("createpost", views.blog, name="blog"),
    path('blog_post/',views.blog_post, name='blog_post'),
    path('django',views.login_admin,name='django'),

    path('admin_home',views.admin_home,name='adminhome'),
    path('add_emp',views.add_emp,name='addemp'),
    path('add_admin',views.add_admin,name='addadmin'),
    path('manageemployees',views.manage_emp,name='manage_emp'),
    path('emp_home',views.employee_home,name='emphome'),
    path('cus_home',views.customer_home,name='cushome'),


    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact_us", views.contact_us, name="contactus"),
    
]
