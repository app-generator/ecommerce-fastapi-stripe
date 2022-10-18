from os import path, listdir
import json

from src import schemas 

def get_local_products():
    products_path = path.expanduser('./src/templates/products')
    products = listdir(products_path)

    product_dicts = []
    for i, product in enumerate(products):
        absolute_path = path.join(products_path, product)
        print (absolute_path)

        with open(absolute_path, 'r') as product_json:
            data = json.load(product_json)
            # verify_product = schemas.ProductBase(data)
            product_dicts.append(data)

    return product_dicts


if __name__=='__main__':
    products = get_local_products()
    print (products)
