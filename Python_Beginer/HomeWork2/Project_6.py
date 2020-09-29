product_repo = []
KEY_PRODUCT_NAME = "название"
KEY_PRODUCT_PRICE = "цена"
KEY_PRODUCT_QUANTITY = "количество"
KEY_QUANTITY_UNIT = "eд"
while True:
    print('1. Ввести товар')
    print('2. Вывести аналитику')
    print('3. Выход')
    enter_select_menu_data = input('Введите пункт меню: ')
    try:
        select_menu = int(enter_select_menu_data)
    except :
        print(f'Введеный номер меню \'{enter_select_menu_data}\' выбран не коректно')
        continue
    if select_menu < 1 or select_menu>3:
        print(f'Введеный номер \'{enter_select_menu_data}\' отсутутствует в меню')
        continue

    if select_menu == 1:
        product_name = input('Введите название продукта: ')
        product_price = input('Введите цену продукта: ')
        product_quantity = input('Введите количество продукта: ')
        quantity_unit = input('Введите единицу измерения количества: ')
        product_repo.append(
            (len(product_repo)+1, 
                {KEY_PRODUCT_NAME: product_name, 
                 KEY_PRODUCT_PRICE: product_price, 
                 KEY_PRODUCT_QUANTITY: product_quantity, 
                 KEY_QUANTITY_UNIT: quantity_unit}))
        continue

    if select_menu == 2:
        product_names = set('')
        product_prices = set('')
        product_quantities = set('')
        quantity_units = set('')
        for product in product_repo:
            product_names.add(product[1].get(KEY_PRODUCT_NAME))
            product_prices.add(product[1].get(KEY_PRODUCT_PRICE))
            product_quantities.add(product[1].get(KEY_PRODUCT_QUANTITY))
            quantity_units.add(product[1].get(KEY_QUANTITY_UNIT))
        analytics = {KEY_PRODUCT_NAME: list(product_names), 
                     KEY_PRODUCT_PRICE: list(product_prices), 
                     KEY_PRODUCT_QUANTITY: list(product_quantities), 
                     KEY_QUANTITY_UNIT: list(quantity_unit)}
        for item in analytics.items():
            print(item)

    if select_menu == 3:
        exit(0)
