shopping_list = ["pizza", "coca-cola", "pepsi", "sprite", "7up"]

item_to_find = "sprite"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

for item in shopping_list:
    if item == item_to_find:
        found_at = shopping_list.index(item)

if found_at is not None:
    print("I have found the item at the position {0}.".format(found_at))
else:
    print("The element is not in your list.")

