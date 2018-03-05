from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.base import View
from . import forms as cart_forms
from apps.books import models as book_models
from apps.manages import models as manage_models


class CartDetailView(View):
    def get(self, request):
        cart = request.user.cart
        hot_books = book_models.Book.get_hot_books()
        return render(request, 'cart.html', {
            'cart': cart,
            'hot_books': hot_books,
        })


class CartAddView(View):
    def get(self, request, book_id):
        book = get_object_or_404(book_models.Book, id=book_id)
        request.user.cart.add(book)
        return HttpResponseRedirect(reverse('cart:detail'))


class CartRemoveView(View):
    def get(self, request, item_id):
        request.user.cart.remove(item_id)
        return HttpResponseRedirect(reverse('cart:detail'))


class CartSettlementView(View):
    def get(self, request):
        settlement_form = cart_forms.SettlementForm()
        recipient = request.user.recipient.order_by('-default').all()
        cart = request.user.cart
        payment_method = manage_models.Payment.objects.all()
        return render(
            request, 'settlement.html', {
                'settlement_form': settlement_form,
                'recipient': recipient,
                'cart': cart,
                'payment_method': payment_method,
            })
