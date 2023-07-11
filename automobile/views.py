from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .forms import LoginForm,CreateUserForm, VechicleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission

from automobile.models import Manufacturer, User, Vechicle

# Create your views here.
# Create your views here.
class Base(View):
    views = {}
class HomeView(Base):
    def get(self,request):
        self.views
        self.views['posts'] = Vechicle.objects.all()
        self.views['vechicle_count'] = Vechicle.objects.all().count()
        return render(request,'index.html',self.views)
# def post_list(request):
#     return render(request,"post_list.html",{"post":posts})

def LOGIN(request):
    form = LoginForm(request.POST or None)
    msg = ''
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('automobile:adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('automobile:staff')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('automobile:stff')
            else:
                messages.error(request,"Invalid Credentials")
        else:
            messages.error(request,'Error in validating forms!!')
    return render(request, 'login.html', {'form': form,'msg': msg})
    context = {} 
    return render(request,'login.html')
def REGISTER(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # if group =
            user = form.cleaned_data.get('username')
            user = User.objects.get(username=user)
            group = Group.objects.get(name="is_staff")
            user.groups.add(group)
            user.save()
            messages.success(request,'Accounts was created for ' + user)
            return redirect('automobile:login')
    context = {'form' :form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('automobile:login')

def adminpage(request):
    vechicle_count = Vechicle.objects.all().count()
    context = {
        'vechicle_count' : vechicle_count
    }
    return render(request,'adminpage.html',context)
def customer(request):
    
    return render(request,'sta.html')
def staff(request):
    vechicle_count = Vechicle.objects.all().count()
    vechicle_post = Vechicle.objects.all()
    user = User.objects.all().count()
    context = {
        'vechicle_count' : vechicle_count,
        'vechicle_post' : vechicle_post,
        'user': user
    }
    return render(request,'staff.html',context)

# def ADD_VECHICLE(request):
#     manufacturer = Manufacturer.objects.all()

#     author = User.objects.all()
#     if request.method == "POST":
#         model = request.POST.get('model')
#         year = request.POST.get('year')
#         image = request.FILES.get('image')
#         price = request.POST.get('price')
#         manufacturer_id = request.POST.get('manufacturer')
#         author_id = request.POST.get('author')
        
#         manufacturer = Manufacturer.objects.get(id = manufacturer_id)
#         author = User.objects.get(id = author_id)
#         vechicle = Vechicle(
#             manufacturer = manufacturer,
#             author = author,
#             model = model,
#             year = year,
#             image = image,
#             price = price,
            
#         )
#         vechicle.save()
#         messages.success(request,'Vechicles Are Successfully Added!')
#         return redirect('add_vechicle')
#     context = {
#         'manufacturer': manufacturer,
#         'author' : author,
#     }
#     return render(request, 'Staff/add_vechicle.html',context)

# def add_vechicle(request):
#     if request.method == 'POST':
#         form = VechicleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('automobile:staff')

#     else:
#         form = VechicleForm()
#     return render(request, 'Staff/add_vechicle.html', {'form': form})    
def delete_vechicle(request, id):
    my_instance = get_object_or_404(Vechicle, id=id)
    if request.method == 'POST':
        my_instance.delete()
        return redirect('automobile:staff')
    
    return render(request, 'staff.html', {'my_instance': my_instance})

# def update_vechicle(request, id):
#     my_instance = get_object_or_404(Vechicle, id=id)
#     if request.method == "GET":
#         form = VechicleUpdateForm(instance=my_instance)
#         return render(request, 'staff/edit_vechicle.html', {'form':form})
#     if request.method == 'POST':
#         form = VechicleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('automobile:staff')
#     # else:
#         # form = VechicleForm(instance=my_instance)
        
#     print(request)
#     return render(request, 'staff/edit_vechicle.html', {'form':form})

def add_update_vechicle(request, id=None):
    if id:
        my_instance = get_object_or_404(Vechicle, id=id)
        form = VechicleForm(request.POST or None,request.FILES or None, instance=my_instance)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return redirect('automobile:staff')
        return render(request,'Staff/edit_vechicle.html',{'form':form})
    else:
        form = VechicleForm(request.POST or None,request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('automobile:staff')
    
    return render(request,'Staff/add_vechicle.html',{'form':form})

def delete_vechicle(request, id):
    vechicle = get_object_or_404(Vechicle, id=id)
    if request.method == 'POST':
        vechicle.delete()
        return redirect('automobile:staff')

    return render(request, 'Staff/delete_vechicle.html', {'instance': vechicle})