from .views import *
from django.urls import path

app_name = "automobile"
urlpatterns = [
    path('',HomeView.as_view(),name='automobile'),
    path('login/',LOGIN,name='login'),
    path('logout/',logoutUser,name='logout'),
    # path('login/', login_view, name='login_view'),
    path('adminpage/', adminpage, name='adminpage'),
    path('customer/', customer, name='customer'),
    path('staff/', staff, name='staff'),
    # path("",post_list,name="post-list")
    path('Staff/Vechicle/Add',add_update_vechicle,name='add_vechicle'),
    path('Staff/Vechicle/edit/<int:id>/',add_update_vechicle,name='update_vechicle'),
    path('Staff/Vechicle/delete/<int:id>/', delete_vechicle, name='delete_vechicle'),

    path('register/',REGISTER,name='register'),
    # path('delete/<int:id>/', delete_vechicle, name='delete_view'),

]