from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem

def landing_page(request):
    return render(request, 'ecommerce/landing_page.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products')
    else:
        form = UserCreationForm()
    return render(request, 'ecommerce/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def products_page(request):
    category_choices = Product.CATEGORY_CHOICES
    products = Product.objects.all()
    return render(request, 'ecommerce/products.html', {
        'products': products,
        'category_choices': category_choices
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect('products')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'ecommerce/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def update_cart(request, item_id):
    # Optional: handle quantity update via POST on cart page
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if request.method == 'POST':
        cart_item.quantity = int(request.POST.get('quantity', cart_item.quantity))
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'ecommerce/place_order.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def confirm_order(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'COD')
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return redirect('view_cart')

        total_price = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(
            user=request.user,
            payment_method=payment_method,
            total_price=total_price
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                item_price=item.product.price
            )
        cart_items.delete()
        return redirect('order_success', order_id=order.id)

    return redirect('place_order')

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'ecommerce/order_success.html', {
        'order': order
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ecommerce/order_history.html', {'orders': orders})
