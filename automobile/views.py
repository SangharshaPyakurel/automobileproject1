from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import LoginForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


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
                return redirect('automobile:admin')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('automobile:customer')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('automobile:staff')
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
            user = form.cleaned_data.get('username')
            messages.success(request,'Accounts was created for ' + user)
            return redirect('automobile:login')
    context = {'form' :form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('automobile:login')

def admin(request):
    return render(request,'admin.html')
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

def ADD_VECHICLE(request):
    manufacturer = Vechicle.objects.all()

    author = User.objects.all()
    if request.method == "POST":
        model = request.POST.get('model')
        year = request.POST.get('year')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        manufacturer = request.POST.get('manufacturer_id')
        author_id = request.POST.get('author')
        
        manufacturer = Vechicle.objects.get(id = manufacturer)
        author = User.objects.get(id = author_id)
        vechicle = Vechicle(
            manufacturer = manufacturer,
            author = author,
            model = model,
            year = year,
            image = image,
            price = price,
            
        )
        vechicle.save()
        messages.success(request,'Vechicles Are Successfully Added!')
        return redirect('add_vechicle')
    context = {
        'manufacturer': manufacturer,
        'author' : author,
    }
    return render(request, 'Staff/add_vechicle.html',context)