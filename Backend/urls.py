from django.urls import path
from Backend import views


urlpatterns=[
    path('index',views.index_page,name="index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('load_backend_auth',views.load_backend_auth,name="load_backend_auth"),
    path('admin_logout',views.admin_logout,name="admin_logout"),

    path('add_category/',views.add_category_page,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('category_details/',views.category_details,name="category_details"),
    path('edit_category_page/<int:cat_id>/',views.edit_category_page,name="edit_category"),
    path('update_category/<int:cat_id>/',views.update_category,name="update_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('product_details/',views.product_details,name="product_details"),
    path('edit_product/<int:pro_id>/',views.edit_product,name="edit_product"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('contact_details/',views.contact_details,name="contact_details"),
]