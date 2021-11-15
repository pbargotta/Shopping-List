class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingList:
    def __init__(self):
        self.items = {}

    def additem(self, additem):
        self.items[additem.name] = additem.price

    def print(self):
        for key in self.items:
            print(f"{key} : £{self.items[key]}")


total_cost = 0
shopping_list = ShoppingList()

add_item = input("Would you like to add an item? ").lower()
if add_item == "yes" or add_item == "y":
    add_item = True
    while add_item:
        item_name = input("What is the name of the item? ")
        item_price = input("How much does the item cost? ")
        print()
        item = Item(item_name, item_price)
        shopping_list.additem(item)

        add_item = input("Would you like to add another item? ").lower()
        if add_item != "yes" and add_item != "y":
            add_item = False
            print()


print("YOUR SHOPPING LIST:")
shopping_list.print()
for item_price in list(shopping_list.items.keys()):
    total_cost += float(shopping_list.items[item_price])
print(f"\nIn total, all your items will cost {total_cost}")
