def add_fruit(inventory, fruit, quantity=0):
    """
    >>> new_inventory = {}
    >>> add_fruit(new_inventory, 'strawberries', 10)
    >>> 'strawberries' in new_inventory
    True
    >>> new_inventory['strawberries']
    10
    >>> add_fruit(new_inventory, 'strawberries', 25)
    >>> new_inventory['strawberries']
    35
    """
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()