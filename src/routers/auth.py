import stripe
from fastapi import APIRouter, HTTPException, status
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

@router.get("/login")
def authorize_stripe():

    response = stripe.OAuth.token(
        grant_type='authorization_code',
        code='ac_MkQOWO8bHm7M3bODX7zVLZXVoNuIqz1M',
    )

    account_id = response['stripe_user_id']

    return {'hip' : account_id}


@router.get("/logout")
def deauthorize_stripe():

    stripe.OAuth.deauthorize(
        client_id='ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb',
        stripe_user_id='acct_5qIK6loErW6kNw'
    )

    return {'hip' : 'hop'}
