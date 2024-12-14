
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def find_index(a, b):
    for index, item in enumerate(b):
        if item == a:
            return index
    return None

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(find_item, items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
