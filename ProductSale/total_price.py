import json


with open('product_data.json') as f:
    data= json.load(f)

sorted_products = sorted(data,key=lambda x : x['totalSales'], reverse=True)

products_price =0
cumulative_percentage=0
products =[]
currency_dict ={'euro':86 , 'doller':76, 'rupee':1 }


for product in sorted_products:
    if product['currency'] != 'rupee':
        product['price'] = product['price'] * currency_dict[product['currency']]
    products_price += product['totalSales']* product['price']

print(products_price)

for product in sorted_products:
    product_percentage = (product['totalSales']*product['price']/products_price)*100
    cumulative_percentage +=product_percentage

    product_dict ={'name':product['name'],
                   'totalSales': product['totalSales'],
                   'product_price': product['totalSales']* product['price'],
                   'percentage':str(int(product_percentage))+'%',
                   'cumulativePercentage':str(int(cumulative_percentage))+'%'}

    products.append(product_dict)
print(json.dumps(products, indent =4))