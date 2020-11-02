import json

with open('product_list.json') as f:
    data= json.load(f)

sorted_products = sorted(data,key=lambda x : x['totalSales'], reverse=True)

all_products_sale =0
cumulative_percentage=0
products =[]

for product in sorted_products:
    all_products_sale += product['totalSales']

for product in sorted_products:
    product_percentage = (product['totalSales']/all_products_sale)*100
    cumulative_percentage +=product_percentage

    product_dict ={'name':product['name'],
                   'totalSales': product['totalSales'],
                   'percentage':str(int(product_percentage))+'%',
                   'cumulativePercentage':str(int(cumulative_percentage))+'%'}

    products.append(product_dict)
print(json.dumps(products, indent =4))