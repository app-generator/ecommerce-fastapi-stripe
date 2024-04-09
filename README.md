# [FastAPI & Stripe](https://blog.appseed.us/fastapi-stripe-free-ecommerce/) `Mini eCommerce`

**[Open-source eCommerce Starter](https://github.com/app-generator/rocket-ecommerce)** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **FastAPI & Stripe**.

<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [Rocket eCommerce](https://appseed.us/product/rocket-ecommerce/django/) | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ Stack: **fastAPI**, `Bootstrap`     | ✅ Stack: **Django**, `TailwindCSS`              | **Everything in PRO**, plus:         |
| ✓ Payments: **Stripe**                | ✅ Payments: **Stripe**                          | ✅ **1mo Custom Development**       | 
| ✓ Minimal Bootstrap Design            | ✅ **Stripe Products Import**                    | ✅ **Team**: PM, Developer, Tester  |
| ✓ No Database                         | ✅ **Local Products Customization**              | ✅ Weekly Sprints                   |
| -                                     | ✅ **Categories**, TAGS                          | ✅ Technical SPECS                  |
| -                                     | ✅ Multi-product **Checkout**                    | ✅ Documentation                    |
| -                                     | ✅ **Discounts Page**                            | ✅ **30 days Delivery Warranty**    |
| -                                     | ✅ **Analytics**                                 | -                                    |
| -                                     | ✅ **Transactions Tracking**                     |  -                                   |
| -                                     | ✅ **Zero Configuration**                        |  -                                   |
| -                                     | ✅ **FIGMA** Project                             |  -                                   |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/) |  -                |
| ------------------------------------  | ------------------------------------              | ------------------------------------|
| -                                     | 🚀 [LIVE Demo](https://rocket-ecommerce.onrender.com/) | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |  

<br />

![FastAPI & Stripe Mini eCommerce - Open-Source Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196479738-be20d203-df44-47ce-a124-d3ed426ef622.jpg)

<br />

## ✨ Quick Start in `Docker`

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

## ✨ Credits & Links

- [FastAPI Framework](https://fastapi.tiangolo.com/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
[FastAPI & Stripe](https://blog.appseed.us/fastapi-stripe-free-ecommerce/) `Mini eCommerce` - Free sample provided by [AppSeed](https://appseed.us).
