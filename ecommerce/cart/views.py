from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart, Account, Order


@login_required
def cart_view(request):
    total = 0
    try:
        user = request.user
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total += i.quantity * i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request, 'cart.html', {'cart': cart, 'total': total})


@login_required
def Add_To_Cart(request, p):
    product = Product.objects.get(id=p)
    user = request.user
    try:
        cart = Cart.objects.get(products=product, user=user)
        if cart.quantity < cart.products.stock:
            cart.quantity += 1
            cart.save()
    except Cart.DoesNotExist:
        cart = Cart.objects.create(products=product, user=user, quantity=1)
        cart.save()

    return redirect('cart:cart_view')


@login_required
def decrement(request, q):
    product = Product.objects.get(id=q)
    user = request.user
    try:
        cart = Cart.objects.get(products=product, user=user)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('cart:cart_view')


@login_required
def delete(request, r):
    user = request.user
    product = Product.objects.get(id=r)
    try:
        cart = Cart.objects.get(products=product, user=user)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')


@login_required
def order(request):
    total = 0
    items = 0
    msg = 0
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        user = request.user
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total += i.quantity * i.products.price
            items += i.quantity

        ac = Account.objects.get(acctnumber=c)
        if float(ac.amount) >= total:
            ac.amount = ac.amount - total
            ac.save()
            for i in cart:
                o = Order.objects.create(user=user, products=i.products, address=a, phone=b, order_status="paid",
                                         noofitems=i.quantity)
                o.save()
            cart.delete()
            msg = "Order Placed Successfully"
            return render(request, 'orderdetail.html', {'msg': msg, 'total': total, 'items': items})
        else:
            msg = "Order Cannot Be Placed"
            return render(request, 'orderdetail.html', {'msg': msg})

    return render(request, 'orderform.html')


def orderview(request):
    user = request.user
    o = Order.objects.filter(user=user, order_status="paid")
    return render(request, 'orderview.html', {'o': o, 'name': user.username})
