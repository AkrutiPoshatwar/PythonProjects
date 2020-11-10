from django.http import JsonResponse
from django.http import HttpResponse
from products.models import Product


def sale_percentage(request):

    products = Product.objects.all()
    total_sale_sum =0
    product_dict = {}

    for product in products:
        total_sale_sum += product.total_sale
    for product in products:
        product_percentage = (product.total_sale/total_sale_sum)*100
        product_dict[product.name] = product_percentage

    return JsonResponse(product_dict)


def total_sale_percent(request):

    products = Product.objects.all().order_by('total_sale')

    total_sale_sum =0
    cumulative_percentage = 0
    product_list =[]
    for product in products:
        total_sale_sum += product.total_sale

    for product in products:
        product_percentage = (product.total_sale/total_sale_sum)*100
        cumulative_percentage += product_percentage

        product_dict = { 'name' : product.name,
                         'total_sale': product.total_sale,
                         'percentage' : str(int(product_percentage))+'%',
                         'cumulativePercentage': str(int(cumulative_percentage))+'%'
                       }
        product_list.append(product_dict)

    return HttpResponse(product_list)


def total_price_percentage(request):

    products = Product.objects.all().order_by('total_sale')
    total_price_sum = 0
    cumulative_percentage = 0
    product_list = []
    currency_dict = {'euro': 86, 'doller': 76, 'rupee': 1}

    for product in products:
        if product.currency != 'rupee':
            product.price += product.price* currency_dict[product.currency]
        total_price_sum += product.total_sale * product.price

    for product in products:
        product_percentage = (product.total_sale * product.price/total_price_sum)*100
        cumulative_percentage +=product_percentage

        product_dict = { 'name': product.name,
                         'total_sale': product.total_sale,
                         'percentage' : str(int(product_percentage))+'%',
                         'cumulativePercentage': str(int(cumulative_percentage))+'%'
                        }
        product_list.append(product_dict)

    return HttpResponse(product_list)
