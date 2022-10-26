# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fastapi import APIRouter, Request, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from src.config import settings
import http3
import stripe


from src import app, schemas

router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))

# Stripe Credentials
stripe_keys = {
    "secret_key"     : settings.stripe_secret_key,
    "publishable_key": settings.stripe_publishable_key,
    "endpoint_secret": settings.stripe_secret_key
}

stripe.api_key = stripe_keys["secret_key"]

@router.get("/", status_code=status.HTTP_200_OK)
async def index(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request" : request})

@router.get("/products/", status_code=status.HTTP_200_OK)
async def products_index(request: Request, response_model=HTMLResponse):
    featured_product_slug = 'featured'
    base_url = request.base_url
    product_url = app.product_router.url_path_for("get_product_by_slug", slug=featured_product_slug)
    request_url = base_url.__str__() + product_url.__str__()[1:]

    http3client = http3.AsyncClient()
    response = await http3client.get(request_url)

    featured_product = response.json()

    products_url = app.product_router.url_path_for("get_products")
    request_url2 = base_url.__str__() + products_url.__str__()[1:]

    http3client = http3.AsyncClient()
    response = await http3client.get(request_url2)

    products = response.json()
    for i,product in enumerate(products):
        if (product['slug']==featured_product_slug):
            del products[i]


    return TEMPLATES.TemplateResponse("ecommerce/index.html", {
        "request" : request,
        "featured_product" : featured_product,
        "products": products,
        })

@router.get("/products/{product_slug}", status_code=status.HTTP_200_OK)
async def product_info(product_slug: str, request: Request, response_model=HTMLResponse):
    base_url = request.base_url
    product_url = app.product_router.url_path_for("get_product_by_slug", slug=product_slug)
    request_url = base_url.__str__() + product_url.__str__()[1:]

    http3client = http3.AsyncClient()
    response = await http3client.get(request_url)

    if (response.status_code==404):
        redirect = RedirectResponse(url=router.url_path_for('products_index'))
        return redirect

    product = response.json()

    return TEMPLATES.TemplateResponse("ecommerce/template.html", {
        "request" : request,
        "product": product,
        "config" : settings
        })

@router.get("/config")
def get_publishable_key():
    stripe_config = {"publicKey" : stripe_keys["publishable_key"]}
    return stripe_config

@router.get("/success")
def success(request: Request):
    return TEMPLATES.TemplateResponse("ecommerce/payment-success.html", {
        "request" : request,
        "config" : settings
        })

@router.get("/cancelled")
def cancelled(request: Request):
    return TEMPLATES.TemplateResponse("ecommerce/payment-cancelled.html", {
        "request" : request,
        "config" : settings
        })


@router.get("/create-checkout-session/{path}/")
async def create_checkout_session(path, request: Request):
    base_url = request.base_url
    product_url = app.product_router.url_path_for("get_product_by_slug", slug=path)
    request_url = base_url.__str__() + product_url.__str__()[1:]

    http3client = http3.AsyncClient()
    response = await http3client.get(request_url)

    product = response.json()


    domain_url = settings.server_address
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - lets capture the payment later
        # [customer_email] - lets you prefill the email input in the form
        # For full details see https:#stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param 

        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": product['name'],
                    "quantity": 1,
                    "currency": 'usd',
                    "amount": product['price'] * 100,
                }
            ]
        )
        return ({"sessionId": checkout_session["id"]})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='There was an error with the stripe session')
        
