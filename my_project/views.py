from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import CreateUserFrom
from django.contrib import messages
from .models import Product, Category, Order, OrderItem
from django.core.paginator import Paginator

def home(request):
    categories = Category.objects.all()
    items = Product.objects.all()
    context = {
        'categories': categories,
        'items': items,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def category(request, cid):
    items = Product.objects.filter(category=cid)
    context = {
        'items': items,
    }
    return render(request, 'product.html', context)

def product(request):
    items = Product.objects.all()
    paginator = Paginator(items, per_page=9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'items': page_obj.object_list,
        'paginator': paginator,
        'page_number': int(page_number)
    }
    return render(request, 'product.html', context)

def product_detail(request, id):
    items = Product.objects.filter(id=id)
    context = {
        'items': items,
    }
    return render(request, 'single-product.html', context)

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account has been created successfully! please, Login to access your account')
            return redirect('login')
    else:
        form = CreateUserFrom()
    return render(request, 'user/register.html', {'form': form})

@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.warning(request, 'email or password incorrect')
    return render(request, 'user/login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def account(request):
    return render(request, 'useraccount.html')

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, completed=False)
        items = order.orderitem_set.all()

    context = {'items': items, 'order': order}
    return render(request, 'shopping-cart.html', context)

@login_required(login_url='login')
def add_to_cart(request, id):
    user = request.user
    items = Product.objects.get(id=id)
    order, created = Order.objects.get_or_create(
        user=user,
        completed=False,
        delivered="pending"
        )
    # quantity = request.POST.get('quantity')
    orderitem, created = OrderItem.objects.get_or_create(order=order, items=items, quantity=1)

    # if action == "decrease":
    #     print("decrease")

    # elif action == "increase":
    #     print("increase")
        
    orderitem.save()
    messages.success(request, 'Item successfully added to your cart')
    return redirect('product_detail', id=id)

@login_required(login_url='login')
def update_quantity(request, id):
    quantity = OrderItem.quantity
    print(quantity)

@login_required(login_url='login')
def delete_item(request, id):
    item = OrderItem.objects.filter(id=id)
    item.delete()
    return redirect('cart')
