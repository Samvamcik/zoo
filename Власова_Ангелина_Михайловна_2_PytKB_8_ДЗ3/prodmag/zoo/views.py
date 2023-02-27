from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import randint
from django.views.decorators.csrf import csrf_exempt

class Animal():
    __max_id = 0
    def __init__(self, category:str, name:str, info:str, price:str):
        self.id = Animal.__max_id
        self.category = category
        self.name = name
        self.info = info
        self.price = price
        Animal.__max_id += 1
    
    def __str__(self):
        return(
            f'ID: {self.id}\n'
            + f'Category: {self.category}\n'
            + f'Name: {self.name}\n'
            + f'Info: {self.info}\n'
            + f'Price: {self.price}\n'
        )

Animals = [Animal('Попугаи', 'Корелла', 'Какаду', '3000 руб.'),
            Animal('','','',''),
            Animal('Собаки', 'Бигль', 'Сиба-ину', '13900 руб.'),
            Animal('Кошки', 'Манчкин', 'Мейн-кун', '45000 руб.'),
            Animal('Черепахи', 'Красноухая черепаха', 'Слоновая черепаха', '10000 руб.')]

def prodzoomag(request):
    aa = randint(0,100)
    return HttpResponse(f'Здравствуйте я Ангелина Власова и мне 16 лет<br> Случайное число: {aa} <br> Название: {Animal.name} <br> Категория: {Animal.category} <br> Цена:{Animal.price}')

zoo = Animal
Animal.category = 'Черепахи'
Animal.name = 'Красноухая черепаха'
Animal.info = 'Слоновая черепаха'
Animal.price = '10000 руб.'

@csrf_exempt
def Animals_view(request: HttpResponse):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        print(repr(category), repr(Animals[-1].category))
        return HttpResponse(',\n\n'.join(str(animal) for animal in Animals
                                        if category is None
                                        or category == animal.category))
    

    if request.method == 'POST':
        body = [element.strip() for element in
                request.body.decode('UTF-8').split('\n')]

        Animals.append(Animal(
            name = body[0],
            category=body[1],
            info = body[2],
            price = int(body[3])
        ))

        return HttpResponse(str(Animals[-1]), status=200)

    return HttpResponse(status=405)


@csrf_exempt
def animal_view(request: HttpResponse, id: int):
    filtered = [Animal for animal in Animals if animal.id == id]

    if len(filtered) == 0:
        return HttpResponse(status=404)

    animal = filtered[0]

    if request.method == 'GET':
        if Animal.name == '':
            return HttpResponseRedirect(reverse('animal'))
            
        return HttpResponse(str("Animal"))

    return HttpResponse(status=405)