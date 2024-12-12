import json
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Book, Register, Login, Order, Cart
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
def index(request):
    return render(request, 'index.html')


def payment(request):
    return render(request, 'payment.html')

class BookListView(ListView):
    model = Book
    template_name = 'list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return super().get_queryset()


class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'

class BookCheckoutview(DetailView):
    model = Book
    template_name = 'checkout.html'

class BookLoginView(LoginView):
    model = Login
    success_url = reverse_lazy('list')
    template_name = 'login.html'



class BookRegisterView(CreateView):
    model = Register
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def PaymentComplete(request):
    body=json.loads(request.body)
    print('BODY:',body)
    product=Book.objects.get(id=body['prosuctId'])
    Order.objects.create(product=product)
    return JsonResponse('Payment completed',safe=False)

class SearchResultsView(ListView):
    model = Book
    template_name = 'list.html'  # Optional: Reuse list.html to simplify templates

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return Book.objects.none()  
    
def add_to_cart(request, product_id):
    Product = get_object_or_404(Book, pk=product_id)
    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        product= Product,
        price=Product.price,
        image_url = Product.image_url,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


