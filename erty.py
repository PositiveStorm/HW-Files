# def get_shop_list_by_dishes(dishes, person_count):
with open('receipts.txt', encoding='utf-8') as file:
    cook_book = {}
    for name in file:
        quantity = int(file.readline())
        list_of_ing = []
        for element in range(quantity):
            element = file.readline().strip().split(' | ')
            dict1 = {'ingridient_name': element[0], 'quantity': element[1], 'measure': element[2].strip()}
            list_of_ing.append(dict1)
        file.readline()
        cook_book[name] = list_of_ing
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    with open('receipts.txt', encoding='utf-8') as file:
        cook_book = {}
        for name in file:
            quantity = int(file.readline())
            list_of_ing = []
            for element in range(quantity):
                element = file.readline().strip().split(' | ')
                dict1 = {'ingridient_name': element[0], 'quantity': element[1], 'measure': element[2].strip()}
                list_of_ing.append(dict1)
                file.readline()
                cook_book[name] = list_of_ing
    # print(cook_book)

    shop_list = {}
    # dishes = ['Омлет', 'Запеченный картофель']
    # person_count = 2
    for dish in dishes:
        if dish in cook_book:
            list_ing = cook_book[dish]
            for ingridient_dict in list_ing:
                name_of_ing = ingridient_dict['ingredient_name']
                if name_of_ing in shop_list:
                    ing_dict = shop_list[ingridient_dict['ingredient_name']]['quantity']
                    shop_list[ingridient_dict['ingredient_name']] = {'measure': ingridient_dict['measure'],
                                                                     'quantity': ingridient_dict['quantity'] * person_count + ing_dict}
                else:
                    shop_list[ingridient_dict['ingredient_name']] = {'measure': ingridient_dict['measure'], 'quantity': ingridient_dict['quantity'] * person_count}

    return shop_list

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)