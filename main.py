from art import *
import os
from pprint import *

def read_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        for l in file:
            recipe_name = l.strip()
            list = []
            ingredients_count = int(file.readline())
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                list.append({'ingredient_name': ingredient_name, 
                                                'quantity': quantity, 
                                                'measure': measure})
            blank_file = file.readline()
            cook_book[recipe_name] = list
    return cook_book


def write_book(cook_book: dict):
    with open('recipes.txt', 'a', encoding='utf-8') as file:
        file.seek(0, 0)
        recipe_names = cook_book.keys()
        for item in recipe_names:
            # count = str(len(cook_book[item]))
            file.write(f'{item}\n')
            file.write(f'{str(len(cook_book[item]))}\n')
            for k in range(len(cook_book[item])):
                ingredients = ''
                for val in cook_book[item][k]:
                    if cook_book[item][k][val] != '':
                        ingredients += str(cook_book[item][k][val]) + ' | '
                    else:
                        ingredients += 'None|'
                ingredients = ingredients[:-3]
                file.write(f'{ingredients}\n')
        file.write(f'' + '\n')
            

def input_recipe():
    recipe = {}
    recipe_name = input('Введите название рецепта: ')
    list = []
    ingredients = {recipe_name: list}
    ingredients_count = int(input('Введите кол-во ингредиентов: '))
    for i in range(ingredients_count):
        ingredient_name = input('Введите название ингредиента: ') 
        quantity = input('Введите кол-во ингредиента: ')
        measure = input('Введите единицу измерения: ')
        list.append({'ingredient_name': ingredient_name, 
                    'quantity': quantity, 
                    'measure': measure})
        recipe[recipe_name] = list
    return recipe

def read_and_print():
    cook_book = read_book()
    recipe_names = cook_book.keys()
    for item in recipe_names:
        print(item)
        for k in range(len(cook_book[item])):
            print(cook_book[item][k])
        print('')

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_book()
    recipe_names = cook_book.keys()

    pprint (cook_book)

    for ingredient_name in cook_book:
        res = f'{element.capitalize()}:\n' + '\n'.join(
            f'{what}, {person_count * how_many}, {EI}' for what, how_many, EI in ingridients)
        print(res)


print(text2art("Cookbook", font='tarty1',chr_ignore=True))
print('\nЧто хотите сделать:\n 1 - добавить рецепт\n 2 - вывести рецепты на экран\n 3 - посчитать расход продуктов')

vyh = True
while vyh == True:
    while True:
        option = int(input('Введите номер опции: '))
        if option < 1 or option > 3:
            print('Такого варианта нет, выберите снова: ')
        else:
            vyh == False
            break

    keys = ['ingredient_name',
        'quantity',
        'measure']

    if option == 1: # Добавить запись
        cook_book = read_book()
        write_book(input_recipe())

    elif option == 2: # вывод записей
        read_and_print()

    elif option == 3: # посчитать сколько надо продуктов на количество людей
        person_count = input('Сколько персон будет обедать?')
        dishes = []
        print ('Введите названия блюд из cook_book для заказа. По завершении заказа введите "*"')
        Xfactor = True
        while Xfactor == True:
            el = input('Название блюда: ')
            if el != '*':
                dishes.append(el)
            else:
                Xfactor = False

        get_shop_list_by_dishes(dishes, person_count)