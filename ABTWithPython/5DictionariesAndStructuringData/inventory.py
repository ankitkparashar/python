# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:22:15 2020

@author: Ankit Parashar
"""
def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+str(k))
        item_total += v
    print("Total number of items: "+str(item_total))
    
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#displayInventory(stuff)
    
