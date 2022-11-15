## Stripe OAuth Setup


👉First, we need get `3 particular credentials` from Stripe. Note that credential 1 and credential 2 have two versions, a test version and a production version. 
1. stripe_publishable_key, it will start with `pk`
2. stripe_secret_key, it will start with `sk`
3. client_id, it will start with `ca` (if you can't find your client ID, keep reading below for more details)


👉Second, we need to set our environment variables to use our stripe credentials. Open the .env file that you should have created during the initial setup (README.md for details) and set the appropriate variables. Note that the stripe_oauth_redirect variable needs to point to your login url, the default should be http://localhost:8000/auth/login


👉Third, now you will go to the Stripe website and add your login url to the list of acceptable redirects. 
1. https://dashboard.stripe.com/test/settings/connect
2. make sure Stripe is in test mode (toggle the switch in the top right corner)
3. go down to the Integration section (here you will also find your test mode client_ID if you couldn't find it before) and under Oauth settings, turn on `Oauth for standard accounts`, and in the redirects section below, add your redirect, which should be: `http://localhost:8000/auth/login` or otherwise match your environment variable


👉 Fourth, now both the app and stripe are setup. You can now register via Stripe oauth. Your products will be loaded automatically, depending on whether or not you're signed in. Users can now sign in/register by following the instructions below:

1. Visit the page `/auth/stripe_login`.
2. You will be redirected to Stripe, login or register (note that you cannot select `skip`, this will result in an error).
3. When you create your account you will automatically be redirected to the `/products` page. Local products will no longer be loaded, user products will. You can login to stripe and add products, they will be reflected on the page upon refresh.
4. You can logout by visiting the page `/auth/logout`. This will restore the local products.