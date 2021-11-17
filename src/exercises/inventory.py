inv = {
    'gold coin': 42, 
    'rope': 1
}
stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42, 
    'dagger': 1,
    'arrow': 12
}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print('{0:^3} {1}'.format(v,k))
        item_total += v
    print('Total number of items: ' + str(item_total))
    print()

def add_to_inventory(inventory: dict, loot: list):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1

if __name__ == '__main__':
    # display_inventory(inv)
    display_inventory(stuff)
    add_to_inventory(stuff, dragon_loot)
    display_inventory(stuff)