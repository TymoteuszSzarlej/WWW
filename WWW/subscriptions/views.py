from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subscription
from django.conf import settings
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/list.html', {'subscriptions': subscriptions})

@login_required
def buy_subscription(request):
    # if request.method == 'POST':
    #     plan = request.POST.get('plan')
    #     price = int(request.POST.get('price'))  # price in cents
    #     session = stripe.checkout.Session.create(
    #         payment_method_types=['card'],
    #         line_items=[{
    #             'price_data': {
    #                 'currency': 'pln',
    #                 'product_data': {'name': plan},
    #                 'unit_amount': price,
    #             },
    #             'quantity': 1,
    #         }],
    #         mode='payment',
    #         success_url=request.build_absolute_uri('/subscriptions/success/'),
    #         cancel_url=request.build_absolute_uri('/subscriptions/cancel/'),
    #     )
        # return redirect(session.url)
    return render(request, 'subscriptions/buy.html')

@login_required
def extend_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk, user=request.user)
    if request.method == 'POST':
        # Example: extend by 1 month
        from datetime import timedelta
        if subscription.end_date:
            subscription.end_date += timedelta(days=30)
            subscription.save()
            messages.success(request, "Subskrypcja przedłużona.")
        return redirect('subscription_list')
    return render(request, 'subscriptions/extend.html', {'subscription': subscription})

@login_required
def delete_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk, user=request.user)
    if request.method == 'POST':
        subscription.delete()
        messages.success(request, "Subskrypcja usunięta.")
        return redirect('subscription_list')
    return render(request, 'subscriptions/delete.html', {'subscription': subscription})

def payment_success(request):
    messages.success(request, "Płatność zakończona sukcesem. Subskrypcja aktywowana.")
    return redirect('subscription_list')

def payment_cancel(request):
    messages.error(request, "Płatność anulowana. Subskrypcja nie została aktywowana.")
    return redirect('subscription_list')
