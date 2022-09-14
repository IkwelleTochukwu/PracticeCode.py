# fantasy game inventory
# inventory.py
stuff = {'rope': 1, 'touch': 6, 'gold-chain': 42, 'dagger': 1, 'arrow': 12, 'bags': 5, 'belts': 34}

def displayInventory(inventory):
    print('inventory:')
    item_total = 0
    for k, v in inventory.items():  # using the for loop to call the key and values for each item.
        print(str(v) + ' '  +  k)
        item_total += v   # this increases the value of item_total for same after each loop
                                        # note that this is just an expression!

    print('Total Number of Items: ' + str(item_total))   # this print the final summisson of the 
                                                         # item_total after the loops.


displayInventory(stuff)

