"""
Program: Warhouse inventory control system
Functionality:
    - Register items to the catalog
        id (auto generate)
        title
        category
        price
        stock
    -Display Catalog
    -Display Catalog (items out of stock)
    -Update the stock of a selected item

    - Print Different Categories

"""
from Menu import print_menu, print_header
from Item import Item
import os
import pickle

catalog = []
id_count = 1
data_file = 'catalog.data'

# methods declaration

def clear():
    return os.system('cls')

def save_catalog():
    writer = open(data_file, "wb") # open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close()

def read_catalog():
    global data_file
    global id_count

    try:
        reader = open(data_file, "rb") # open a file to Read Binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)
    
        last = catalog[-1] # get the last element from the array
        id_count = last.id + 1

        how_many = len(catalog)
        print(" Loaded " + str(how_many) + " Items")
    except:
        # when the code above crashes, we get here
        print(" *Error loading data!")

def register_item():
    global id_count # import the global variable into function scope
    print_header('  Register new Item')
    title = input('Please input the title: ')
    category = input('Please input the Category: ')
    price = float(input('Please input the Price: '))
    stock = int(input('Please input the Stock: '))
    # do validations here

    # create the object
   
    new_item = Item() # <-- how to create an object of a class
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    
    id_count += 1
    catalog.append(new_item)
    print("   Item created!")

def display_catalog():
    num_items = len(catalog) # <- get length of array or string
    print_header(' Catalog contains ' + str(num_items) )
    print(' | ID  | Title                | Category          |     Price |    Stock ')
    print('-' * 80)



    for item in catalog:
        print(" | " + str(item.id).ljust(3) 
            + " | " + item.title.ljust(20)
            + " | " + item.category.ljust(17)
            + " | " + str(item.price).rjust(9)
            + " | " + str(item.stock).rjust(5) )
    
    print('-' * 80)

def print_stock_value():
    total = 0
    for item in catalog:
        total += (item.stock * item.price)
    print("Warehouse Value: $" + str(total))




def display_no_stock():
    print_header(' Item Out of Stock ')
    print('| Title              | Category          |     Price |    Stock ')
    print('-' * 80)



    for item in catalog:
        if(item.stock == 0):
            print(item.title.ljust(20)
                + " | " + item.category.ljust(17)
                + " | " + str(item.price).rjust(9)
                + " | " + str(item.stock).rjust(5) )

    print('-' * 80)

def remove_item():
    # show the list of items
    # ask the user to choose an id to remove
    # validate the id
    # remove the item

    display_catalog()
    selected = int(input('Please select the ID to remove  '))

    found = False
    for item in catalog:
        if(item.id == selected):
            delete_stock = input(" Are you sure you want to remove " + item.title + " from inventory? ")
            found = True
            if("yes"):
                catalog.remove(item)
            
            
    if(found == False):
        print('** Error: Selected ID Does not exist, try again')

def categories():
    print_header(" Categories In Warehouse")
    already_printed = []
    for item in catalog:
        if item.id > 0 and not item.category in already_printed:
            print(item.category)
            already_printed.append(item.category)



def update_stock():
    # show all the items
    # ask the user to choose an id
    # validate the selected id
    # ask for the new stock value
    #update the stock value of the selected items
    display_catalog()
    selected = int(input(' Please select the ID to update '))

    found = False
    for item in catalog:
        if(item.id == selected):
            print(' ID is found')
            new_stock = input(' Please input new stock value: ')
            item.stock = int(new_stock)
            found = True
            print(' Updated! ')
    if(found == False):
        print('** Error: Selected ID Does not exist, try again')
    # here

read_catalog()

# loop to display menu

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Select an option: ')

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        update_stock()
        save_catalog()
    elif(opc == '5'):
        print_stock_value()
    elif(opc == '6'):
        remove_item()
        save_catalog()
    elif(opc == '7'):
        categories()

    input('Press Enter to Continue... ')