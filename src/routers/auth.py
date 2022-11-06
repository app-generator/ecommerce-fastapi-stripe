import stripe
from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from src import app
from src.config import settings

router = APIRouter(
    prefix = "/auth",
    tags = ['Auth']
)

# Stripe Credentials
stripe_keys = {
    "secret_key"     : settings.stripe_secret_key,
    "publishable_key": settings.stripe_publishable_key,
    "endpoint_secret": settings.stripe_secret_key
}

stripe.api_key = stripe_keys["secret_key"]

@router.get("/stripe_login")
def stripe_login(request: Request):
    base_url = request.base_url
    login_url = app.auth_router.url_path_for("authorize_stripe")
    redirect_uri = base_url.__str__() + login_url.__str__()[1:]

    client_id = 'ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb'
    stripe_login_url = f'https://connect.stripe.com/oauth/authorize?response_type=code&client_id={client_id}&scope=read_write&redirect_uri={redirect_uri}'

    redirect = RedirectResponse(url=stripe_login_url)

    stripe.api_key = stripe_keys["secret_key"]

    return redirect



@router.get("/login")
def authorize_stripe(request: Request):
    authorization_code = request.query_params.get('authorization_code')
    # response = stripe.OAuth.token(
    #     grant_type='authorization_code',
    #     code='ac_MkQOWO8bHm7M3bODX7zVLZXVoNuIqz1M',
    # )

    # account_id = response['stripe_user_id']

    return {'hip' : 'hop'}
    


@router.get("/logout")
def deauthorize_stripe():

    stripe.OAuth.deauthorize(
        client_id='ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb',
        stripe_user_id='acct_5qIK6loErW6kNw'
    )

    return {'hip' : 'hop'}
