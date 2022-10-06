from os import getcwd


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for dish in dishes:
        if dish not in cook_book:
            raise TypeError('dish not found in cook_book')
        else:
            for ingredient in cook_book[dish]:
                dish_name = ingredient['ingredient_name']
                if dish_name not in ingredient_dict:
                    ingredient_dict[dish_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    ingredient_dict[dish_name]['quantity'] += ingredient['quantity'] * person_count
    return ingredient_dict


directory = getcwd()
cook_book = {}

with open(directory + r'\Recipes.txt', 'r', encoding='UTF-8') as file:
    for recipes in file:
        cook_book[recipes.strip()] = []
        for i in range(int(file.readline())):
            name, quan, meas = file.readline().strip().split(' | ')
            cook_book[recipes.strip()].append(
                {'ingredient_name': name,
                 'quantity': int(quan),
                 'measure': meas}
            )
        file.readline()
