from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import randint
from django.views.decorators.csrf import csrf_exempt

class Product():
    __max_id = 0
    def __init__(self, category:str, name:str, info:str, price:str):
        self.id = Product.__max_id
        self.category = category
        self.name = name
        self.info = info
        self.price = price
        Product.__max_id += 1
    
    def __str__(self):
        return(
            f'ID: {self.id}\n'
            + f'Category: {self.category}\n'
            + f'Name: {self.name}\n'
            + f'Info: {self.info}\n'
            + f'Price: {self.price}\n'
        )

products = [Product('Мясная продукция', 'Колбаса', 'Колбаса докторская', '300 руб.'),
            Product('','','',''),
            Product('Газированные напитки', 'Кола', 'Кола Добрый', '129 руб.'),
            Product('Хлебобулочные изделия', 'хлеб', 'Хлеб чёрный', '35 руб.'),
            Product('Молочная продукция', 'Молоко', 'Молоко 2.5', '100 руб.')]

def prodmag(request):
    aa = randint(0,100)
    return HttpResponse(f'Привет я Артём Баскаков и мне 14 лет<br> Случайное число: {aa} <br> Название: {prod.name} <br> Категория: {prod.category} <br> Цена:{prod.price}')

prod = Product
prod.category = 'Молочная продукция'
prod.name = 'Молоко'
prod.info = 'Молоко 2.5'
prod.price = '100 руб.'

@csrf_exempt
def products_view(request: HttpResponse):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        print(repr(category), repr(products[-1].category))
        return HttpResponse(',\n\n'.join(str(product) for product in products
                                        if category is None
                                        or category == product.category))
    

    if request.method == 'POST':
        body = [element.strip() for element in
                request.body.decode('UTF-8').split('\n')]

        products.append(Product(
            name = body[0],
            category=body[1],
            info = body[2],
            price = int(body[3])
        ))

        return HttpResponse(str(products[-1]), status=200)

    return HttpResponse(status=405)


@csrf_exempt
def product_view(request: HttpResponse, id: int):
    filtered = [product for product in products if product.id == id]

    if len(filtered) == 0:
        return HttpResponse(status=404)

    product = filtered[0]

    if request.method == 'GET':
        if product.name == '':
            return HttpResponseRedirect(reverse('products'))
            
        return HttpResponse(str(product))

    return HttpResponse(status=405)