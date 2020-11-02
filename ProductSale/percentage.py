import json

with open('product_list.json') as f:
    data= json.load(f)


all_products_sale =0
for product in data:
    all_products_sale += product['totalSales']

for product in data:
    product_percentage = (product['totalSales']/all_products_sale)*100
    print(product['name'],product_percentage,'%')
