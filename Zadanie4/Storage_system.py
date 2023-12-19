print('****************** \n Beginning of program. Lets start \n *************** \n')
account = float(0)
warehouse_list = []
quantity_of_items = []
prices = []
command_list = ['balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'overview', 'commands', 'exit']
# Pozycja w liscie:  0        1          2          3        4          5           6           7         9
#print(f'List of commands: {command_list}')
print(f'Your account balance at the beginning of the program: {account}')
print(f'The state of your warehouse at the beginning of the program: {warehouse_list}')
print(f'Prices of your items at warehouse on the beginning of the program: {prices}')

while True:
    print(f'List of commands: {command_list}')
    command = input('What command do you want to use? \n')

    if command == 'balance':
        command_balance = input('Do you want to add or subtract an amount? You can use only add or subtract here: \n')
        if command_balance == 'add':
            value = float(input('Specify the value you want to add: \n'))
            account += value
            print(account)
        elif command_balance == 'subtract':
            value = float(input('Specify the value you want to add: \n'))
            account -= value
            print(account)
        else:
            print('You must provide the value in numbers, try again. \n')
            continue

    elif command == 'sale':
        item = input('What do You want to sale?: \n')
        if item in warehouse_list:
            warehouse_list.index(item)
            quantity = int(input('How many pieces do You want to sale?: \n'))
            if quantity_of_items[warehouse_list.index(item)] >= quantity:
                quantity_of_items[warehouse_list.index(item)] = quantity_of_items[warehouse_list.index(item)] - quantity
                new_value = quantity * prices[warehouse_list.index(item)]
                account += new_value
                if quantity_of_items[warehouse_list.index(item)] == 0:
                    quantity_of_items.remove(warehouse_list.index(item))
                    prices.remove(prices[warehouse_list.index(item)])
                    warehouse_list.remove(warehouse_list[warehouse_list.index(item)])
                    continue
        else:
            print(f'{item} not in store. Try again. \n')
            continue

    elif command == 'purchase':
        item = input('What do You want to buy?: \n')
        if item not in warehouse_list:
            quantity = int(input('How many pieces do You want to buy?: \n'))
            piece_price = float(input('How much for piece?: \n'))
            price_of_all = float(quantity*piece_price)
            if price_of_all <= account:
                print(f'You have just bought: {item}, {quantity} pieces, for {price_of_all}. \n')
                account -= price_of_all
                warehouse_list.append(item)
                quantity_of_items.append(quantity)
                prices.append(piece_price)
                print(f'Current lists: \n Yours items at warehouse: {warehouse_list}, \n How many at store: {quantity_of_items}, \n How much for each: {prices}. \n')
                continue
            else:
                price_of_all > account
                print(f'You dont have enough money on account. You have {account}. Try again. \n')
                continue
        elif item in warehouse_list:
            yes_or_no = input(f'You have this {item} in store. Do You want buy some pieces? (Yes/No): \n')
            if yes_or_no == 'Yes' or yes_or_no == 'yes':
                quantity = int(input('How many pieces do You want to buy?: \n'))
                warehouse_list.index(item)
                prices[warehouse_list.index(item)]
                new_value = quantity * prices[warehouse_list.index(item)]
                if new_value <= account:
                    print('You bought new pieces. \n')
                    account -= new_value
                    quantity_of_items[warehouse_list.index(item)] = quantity + quantity_of_items[warehouse_list.index(item)]
                    continue
                elif new_value > account:
                    print('You dont have enough money on account. \n')
            elif yes_or_no == 'No' or yes_or_no == 'no':
                print(f'You dont have enough money on account. You have {account}. Try again. \n')
                continue
        else:
            print('Wrong command, try again. \n')
            continue

    elif command == 'account':
        print(f'Your account balance is: {account}')
        continue

    elif command == 'list':
        print(f'In Your store: \n {warehouse_list}, \n {quantity_of_items}, \n {prices}. \n')
        continue

    elif command == 'warehouse':
        item = input('Input name of item: \n')
        if item in warehouse_list:
            print(f'Position in store: {warehouse_list.index(item)}')
            print(f'Number in item in store: {quantity_of_items[warehouse_list.index(item)]}')
            print(f'How many cost: {prices[warehouse_list.index(item)]} \n')
        else:
            print('Wrong name of item. \n')

    elif command == 'overview':
        overview_start = input('Specify the beginning of the list (write number): \n')
        overview_end = input('Specify the end of the list (write number): \n')
        overview_on_start = 0
        overview_on_start += int(overview_start)
        overview_on_end = 0
        overview_on_end += int(overview_end)
        if overview_start == '' and overview_end == '':
            print('In store is: ')
            print(f'{warehouse_list[0 : -1]}')
            print(f'{quantity_of_items[0 : -1]}')
            print(f'{prices[0 : -1]} \n')
            continue
        elif overview_on_start >= 0 and overview_end == '':
            print('In store is: ')
            print(f'{warehouse_list[overview_on_start : -1]}')
            print(f'{quantity_of_items[overview_on_start : -1]}')
            print(f'{prices[overview_on_start : -1]} \n')
            continue
        elif overview_on_end <= -1 and overview_start == '':
            print('In store is: ')
            print(f'{warehouse_list[0: overview_on_end]}')
            print(f'{quantity_of_items[0: overview_on_end]}')
            print(f'{prices[0: overview_on_end]} \n')
            continue
        elif overview_on_start >= 0 and overview_on_end >= 0 or overview_on_end <= 0:
            print('In store is: ')
            print(f'{warehouse_list[overview_on_start: overview_on_end]}')
            print(f'{quantity_of_items[overview_on_start: overview_on_end]}')
            print(f'{prices[overview_on_start: overview_on_end]} \n')
        elif overview_on_start <= -1:
            print(f'Error try between zero and amount items in your list. \n Your list: {warehouse_list.copy()} \n')
        elif overview_on_end >= 0:
            print(f'Error try between zero and amount items in your list. \n Your list: {warehouse_list.copy()} \n')

    elif command == 'commands':
        print(f'Command list: {command_list} \n')

    elif command == 'exit':
        print('Here the program ends. Goodbye. \n')
        break

    else:
        print('There is no such command, try again. \n')
        continue
