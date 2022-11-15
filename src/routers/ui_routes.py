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
import json


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

    access_key = request.cookies.get('Stripe-Account')

    if (access_key):
        # print ('here is where we can determine if local products or stripe products get loaded')
        stripe.api_key = access_key
        # stripe.

        json_data = []
        products = stripe.Product.list(expand = ['data.default_price'])
        print ('\n\n')
        print (products)
        print ('\n\n')
        productdict = []
        for product in products:
            dict= {}
            dict['id'] = product['id']
            dict['name'] = product['name']
            dict['price'] = product["default_price"]["unit_amount"]/100
            dict['currency'] = product["default_price"]["currency"]
            dict['full_description'] = product["description"]
            dict['info'] = product["description"][0:30]

            for index, image in enumerate(product['images']):
                dict['img_main'] = image

            dict['img_card'] = ''
            dict['img_1'] = ''
            dict['img_2'] = ''
            dict['img_3'] = ''

            productdict.append(dict)
        
        for product in productdict:
            json_product = json.dumps( product, indent=4, separators=(',', ': ') )
            json_data.append(json_product)

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
        

@router.get("/success")
def success(request: Request):
    return TEMPLATES.TemplateResponse("ecommerce/payment-success.html", {
        "request" : request,
        "config" : settings
    })

@router.get("/presentation")
def presentation(request: Request):
    return TEMPLATES.TemplateResponse("pages/presentation.html", {
        "request" : request,
        "config" : settings
    })


@router.get("/page-about-us")
def page_about_us(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-about-us.html", {
        "request" : request,
        "config" : settings
    })


@router.get('/page-contact-us')
def page_contact_us(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-contact-us.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-author')
def page_author(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-author.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-sign-in')
def page_sign_in(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-sign-in.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-sign-up')
def page_sign_up(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-sign-up.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-404')
def page_404(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-404.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-sections-hero-sections')
def page_sections_hero_sections(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-sections-hero-sections.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/page-sections-features')
def page_sections_features(request: Request):
    return TEMPLATES.TemplateResponse("pages/page-sections-features.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/navigation-navbars')
def navigation_navbars(request: Request):
    return TEMPLATES.TemplateResponse("pages/navigation-navbars.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/navigation-nav-tabs')
def navigation_nav_tabs(request: Request):
    return TEMPLATES.TemplateResponse("pages/navigation-nav-tabs.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/navigation-pagination')
def navigation_pagination(request: Request):
    return TEMPLATES.TemplateResponse("pages/navigation-pagination.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/input-areas-inputs')
def input_areas_inputs(request: Request):
    return TEMPLATES.TemplateResponse("pages/input-areas-inputs.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/input-areas-forms')
def input_areas_forms(request: Request):
    return TEMPLATES.TemplateResponse("pages/input-areas-forms.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/attention-catchers-alerts')
def attention_catchers_alerts(request: Request):
    return TEMPLATES.TemplateResponse("pages/attention-catchers-alerts.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/attention-catchers-modals')
def attention_catchers_modals(request: Request):
    return TEMPLATES.TemplateResponse("pages/attention-catchers-modals.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/attention-catchers-tooltips-popovers')
def attention_catchers_tooltips_popovers(request: Request):
    return TEMPLATES.TemplateResponse("pages/attention-catchers-tooltips-popovers.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-buttons')
def elements_buttons(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-buttons.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-avatars')
def elements_avatars(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-avatars.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-dropdowns')
def elements_dropdowns(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-dropdowns.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-toggles')
def elements_toggles(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-toggles.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-breadcrumbs')
def elements_breadcrumbs(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-breadcrumbs.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-badges')
def elements_badges(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-badges.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-typography')
def elements_typography(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-typography.html", {
        "request" : request,
        "config" : settings
    })

@router.get('/elements-progress-bars')
def elements_progress_bars(request: Request):
    return TEMPLATES.TemplateResponse("pages/elements-progress-bars.html", {
        "request" : request,
        "config" : settings
    })

