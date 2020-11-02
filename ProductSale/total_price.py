import json

def main(path ='product_data.json'):

    with open(path) as f:
        data = json.load(f)

    sorted_products = sorted(data, key=lambda x: x['totalSales'], reverse=True)

    total_price = 0
    cumulative_percentage = 0
    products_list = []
    currency_dict = {'euro': 86, 'doller': 76, 'rupee': 1}

    for product in sorted_products:

        if product['currency'] != 'rupee':
            product['price'] = product['price'] * currency_dict[product['currency']]
        total_price += product['totalSales']* product['price']

    for product in sorted_products:
        
        percentage = (product['totalSales']*product['price']/total_price)*100
        cumulative_percentage +=percentage

        product_dict ={'name':product['name'],
                       'totalSales': product['totalSales'],
                       'percentage':str(int(percentage))+'%',
                       'cumulativePercentage':str(int(cumulative_percentage))+'%'}

        products_list.append(product_dict)
    print(json.dumps(products_list, indent =4))


if __name__ == "__main__":
    main()
