def cook_dict():

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



cook_dict()




