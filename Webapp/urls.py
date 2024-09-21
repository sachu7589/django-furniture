from django.urls import path
from Webapp import views

urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('category_page/<str:category_name>/',views.category_page,name="category_page"),
    path('product_page/',views.product_page,name="product_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('register_page/',views.main_register_page,name="register_page"),
    path('save_reg/',views.save_reg,name="save_reg"),
    path('payment_page/',views.payment_page,name="payment_page"),
]