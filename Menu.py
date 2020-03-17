def print_menu():
    print('-' * 80)
    print('  The Snake Way - Welcome ')
    print('-' * 80)

    print('[1] Register New Item')
    print('[2] Display Inventory')
    print('[3] Show Out of Stock Items')
    print('[4] Update Stock Manually')
    print('[5] Show the Total Value of the Inventory')
    print('[6] Remove Items from Inventory')
    print('[7] Display Categories')

    print('[x] Exit')

def print_header(title):
    print('\n\n') # 2 blank lines
    print('-' * 30)
    print(title)
    print('-' * 30)