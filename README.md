# FastAPI & Stripe `Mini eCommerce`

**Open-source eCommerce Starter** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **FastAPI & Stripe**.

- [FastAPI mini eCommerce](https://github.com/app-generator/ecommerce-fastapi-stripe) sources (this repo)
- [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/) - **PRO Version**
  - ✅ Stripe Integration
  - ✅ Checkout, Discounts Page
  - ✅ Tags, Categories
  - ✅ Analytics
  - ✅ Generated Sitemap
  
<br />

## Quick Start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-fastapi-stripe.git
$ cd ecommerce-fastapi-stripe
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ Manual Build

The process is basically the usual set up for any Python app: `environment` set up, `dependencies` install, and `bootstrap`. 

<br />

> 👉 **Step 1** - `Download the code` from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-fastapi-stripe.git
$ cd ecommerce-fastapi-stripe
```

<br />

> 👉 **Step 2** - Rename `env.sample` to `.env` and provide the Stripe Secrets

- Edit `STRIPE_SECRET_KEY` - provided by Stripe Platform
- Edit `STRIPE_PUBLISHABLE_KEY` - provided by Stripe Platform

<br />

> 👉 **Step 3** - `Install dependencies`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 **Step 4** - `Start the App`

```bash
$ uvicorn src.app:app --reload
```

Visit `http://localhost:8000` in your browser. For another port, use `--port 8099` directive.

<br />

## ✨ Create a new Product

- Go to `src/templates/products` directory
- Create a new `JSON` file with data:
  - `name`: Used in product page & Cards
  - `price`: Used for payment
  - `currency`: Used for payment
  - `info`: used in cards 
  - `short_description`: used in product page
  - `full_description`: used in product page
- Create Media Files
  - Go to `src/static/products` 
  - Create a directory using the same name as for `JSON` file
    - Create `card.jpg`: 500x335px
    - Create `cover.jpg`: 2100x1400px
- Start or refresh the app
  - The new product should be listed in the `products/` page
  - Product page is available at address:
    - `http://localhost:8000/products/<SLUG>/` where the SLUG is the name of the JSON file 
  
<br />

> Sample product page generated for [Air ZOOM Pegasus](./src/templates/products/air-zoom-pegasus.json), assets loaded from [here](./src/static/products/air-zoom-pegasus)

<br />

## Need More? Go PRO with [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/)

Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support - Actively supported by [App-Generator](https://app-generator.dev/).

| Status | Item | info | 
| --- | --- | --- |
| ✅ | Stack | Django, Tailwind, React |
| ✅ | Payments | Stripe |
| ✅ | Categories | YES |
| ✅ | Tags | YES |
| ✅ | Checkout | YES |
| ✅ | Discounts Page | YES |
| ✅ | Products Import | Stripe |
| ✅ | Products Local Customization | YES |
| ✅ | Analitycs | Weekly, Monthly, Year `Sales` |
| ✅ | Transactions Tracking | YES |
| ✅ | Docker | YES |
| ✅ | CI/CD | Render |

![Rocket eCommerce - Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support.](https://github.com/user-attachments/assets/5db5841f-6802-4dfa-8ce7-46cf14435c5a)

<br />

---
FastAPI & Stripe `Mini eCommerce` - Open-source eCommerce Starter provided by [App-Generator](https://app-generator.dev/).

