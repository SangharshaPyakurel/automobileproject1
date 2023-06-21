from .views import *
from django.urls import path
app_name = "automobile"
urlpatterns = [
    path('',HomeView.as_view(),name='automobile'),
    path('login/',LOGIN,name='login'),
    path('logout/',logoutUser,name='logout'),
    # path('login/', login_view, name='login_view'),
    path('admin/', admin, name='admin'),
    path('customer/', customer, name='customer'),
    path('staff/', staff, name='staff'),
    # path("",post_list,name="post-list")
    path('Staff/Vechicle/Add',ADD_VECHICLE,name='add_vechicle'),

    path('register/',REGISTER,name='register'),

]