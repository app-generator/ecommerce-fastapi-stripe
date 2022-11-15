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
    if not settings.stripe_client_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing a Required Credential, Stripe Client ID, check your environment variables")

    stripe_login_url = f'https://connect.stripe.com/oauth/authorize?response_type=code&client_id={settings.stripe_client_id}&scope=read_write&redirect_uri={settings.stripe_oauth_redirect}'
    redirect = RedirectResponse(url=stripe_login_url)

    return redirect

@router.get("/login")
def authorize_stripe(request: Request):
    authorization_code = request.query_params.get('code')
    try:
        response = stripe.OAuth.token(
            grant_type='authorization_code',
            code=authorization_code,
        )
        
        stripe_user_id = response['stripe_user_id']
        access_token = response['access_token']

        redirect = RedirectResponse(url=app.ui_router.url_path_for('products_index'))
        redirect.status_code = 302
        redirect.set_cookie('Stripe-Account', access_token)
        redirect.set_cookie('Stripe-User-ID', stripe_user_id)

        return redirect
    except Exception as e:
        print (e)
        print ('login error')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Missing Authorization Code")

@router.get("/logout")
def deauthorize_stripe(request: Request):
    try:
        stripe_user_id = request.cookies.get('Stripe-User-ID')
        access_key = request.cookies.get('Stripe-Account')

        if (not stripe_user_id or not access_key):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="TYou are not logged in")

        stripe.api_key = stripe_keys['secret_key']

        stripe.OAuth.deauthorize(
            client_id=settings.stripe_client_id,
            stripe_user_id=stripe_user_id
        )

        redirect = RedirectResponse(url=app.ui_router.url_path_for('index'))
        redirect.status_code = 302
        redirect.set_cookie('Stripe-Account', '')
        redirect.set_cookie('Stripe-User-ID', '')

        return redirect
    except Exception as e:
        print (e)
        # request.cookies.update()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization Code")
