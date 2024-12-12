from django import urls
from .import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import BookListView, BookDetailView, BookCheckoutview, BookLoginView, BookRegisterView, PaymentComplete, \
    SearchResultsView

urlpatterns = [
    path('book_list/',BookListView.as_view(),name = 'list'),
    path('payment/',views.payment,name='payment'),
    path('details/<int:pk>/',BookDetailView.as_view(),name = 'detail-view'),
    path('checkout/<int:pk>/',BookCheckoutview.as_view(),name = 'checkout-view'),
    path('login/', BookLoginView.as_view(),name='login'),
    path('register/', BookRegisterView.as_view(),name='register'),
    path('complete/', views.PaymentComplete,name='complete'),
    path('logout/', LogoutView.as_view(next_page='register'), name='logout'),
    path('search/',SearchResultsView.as_view(),name='search'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
]