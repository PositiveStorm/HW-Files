# def cook_dict():
#     cook_book = {}
#     list_of_ing = []
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
    print(cook_book)



    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            list_ing = cook_book[dish]
            for ingridient_dict in list_ing:
                name_of_ing = ingridient_dict['ingredient_name']
                shop_list[name_of_ing] = {'measure': ingridient_dict['measure'], 'quantity':(ingridient_dict['quantity'] * person_count)}
            for ing in shop_list:
                name1 = shop_list[name_of_ing]
                if name_of_ing == ing:
                    name1['quantity'] += name1['quantity']
                else:
                    name1['quantity'] = name1['quantity']
    print(shop_list)
get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 3)




