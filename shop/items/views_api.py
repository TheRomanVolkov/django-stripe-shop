from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from .models import Item
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        item = get_object_or_404(Item, id=id)
        data = {
            'name': item.name,
            'description': item.description,
            'price': item.price
        }
        return Response(data)


class CreateCheckoutSessionAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/') + '?success=true',
            cancel_url=request.build_absolute_uri('/') + '?canceled=true',
        )
        return Response({'id': session.id})
