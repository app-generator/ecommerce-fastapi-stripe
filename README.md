# FastAPI & Stripe `Mini eCommerce`

Open-source mini `eCommerce` project that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **FastAPI**.

<br />

> Roadmap & Features 

| Status | Item | info | 
| --- | --- | --- |
| ✅ | **FastAPI** | For `backend logic` |
| ✅ | **Stripe** | `Payment processor` |
| ✅ | **[Soft UI Design](https://www.creative-tim.com/product/soft-ui-design-system?AFFILIATE=128200)** | (Free Version) by `Creative-Tim` |
| ✅ | **JSON** | `Products definition` - see [sample](./app/templates/products/product-air-zoom-pegasus.json) |
| ✅ | Automatic Products Discovery | Source DIR: [templates\products](./src/templates/products) |
| ❌ | **Deployment** | `Docker` & Pages Compression |
| ❌ | **CI/CD** | Render Deployment Platform |

<br />

## ✨ Start the app in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/sample-fastapi-stripe.git
$ cd sample-fastapi-stripe
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />


## Manual Build

> 👉 Rename `env.sample` to `.env` and provide the Stripe Secrets

- Edit `STRIPE_SECRET_KEY` - provided by Stripe Platform
- Edit `STRIPE_PUBLISHABLE_KEY` - provided by Stripe Platform

<br />

> 👉 Install dependencies

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Start the App

```bash
$ uvicorn src.app:app --reload
```

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

> Sample product page generated for [Air ZOOM Pegasus](./src/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](./src/static/products/product-air-zoom-pegasus)

<br />

## ✨ Credits & Links

- [FastAPI Framework](https://fastapi.tiangolo.com/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
FastAPI & Stripe `Mini eCommerce` - Free sample provided by [AppSeed](https://appseed.us).
