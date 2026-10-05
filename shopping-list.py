shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": False},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False}
]

items = [x["item"] for x in shopping_list if not x["purchased"]]
cost = sum([x["price"] for x in shopping_list if not x["purchased"]])

print("Still need to buy:", items)
print("Remaining cost:", cost)