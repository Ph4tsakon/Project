from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product

def index(request):
    products = Product.objects.all()  # Fetch all products to display on the homepage
    return render(request, 'index.html', {'products': products})

def login(request):
    return render(request, 'login.html')

def list_view(request):
    return render(request, 'list.html')

def signup(request):
    return render(request, 'signup.html')

def AP(request):
    return render(request, 'AP.html')


def P1(request):
    return render(request, 'P1.html')
def P2(request):
    return render(request, 'P2.html')
def P3(request):
    return render(request, 'P3.html')
def P4(request):
    return render(request, 'P4.html')
def P5(request):
    return render(request, 'P5.html')

def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use')
                return redirect('signup')
            else:
                User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                messages.success(request, 'User registered successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    return redirect('signup')

def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('index')
        messages.error(request, 'Invalid username or password')
    return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('index')

def submit_product(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_content = request.POST.get("product")  # Get product content from form
        pd_id = request.POST.get("pd_id", "")  # Assuming pd_id is also sent from form
        
        Product.objects.create(
            user=request.user,
            content=product_content,
            pd=pd_id
        )
        messages.success(request, 'Product submitted successfully')
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    return HttpResponse("Unauthorized", status=401)

def delete_product(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id, user=request.user)
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    return HttpResponse("Unauthorized", status=401)

def list(request):
    return render(request, 'list.html')