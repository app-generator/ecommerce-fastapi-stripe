import json
from os import path, listdir
from venv import create

from src import schemas 

def create_slug(json_file_name):
    filename, _blank = json_file_name.split('.json')
    return filename

def get_local_products():
    products_path = path.expanduser('./src/templates/products')
    products = listdir(products_path)

    product_dicts = []
    for product in products:
        absolute_path = path.join(products_path, product)

        with open(absolute_path, 'r') as product_json:
            data = json.load(product_json)
            try:
                product_slug = create_slug(product)
                data['slug'] = product_slug
                verify_product = schemas.ProductBase(**data)
                product_dicts.append(data)
            
            except Exception as e:
                print( 'Err: ' + str(e) )
                continue

    return product_dicts

