def cook_dict():
    cook_book = {}
    list_of_ing = []
    with open('receipts.txt', encoding='utf-8') as file:
        name = file.readline()
        quantity = file.readline()
        quantity = int(quantity)
        for element in range(quantity):
            element = file.readline().strip().split(' | ')
            dict1 = {'ingridient_name': element[0], 'quantity': element[1], 'measure': element[2].strip()}
            list_of_ing.append(dict1)

        cook_book[name] = list_of_ing
        print(cook_book)
cook_dict()


