# *Дополнительное задание:
# программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
class Store():
#  класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена.

# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес,
# а также пустой словарь для `items`
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}

# - метод для добавления товара в ассортимент
    def add_items(self,key,price):
        self.items.update({key: price})
#- метод для удаления товара из ассортимента.
    def delete_item(self,key):
        if key in self.items:
            self.items.pop(key)
        else:
            print(f'Товар "{key}" не найден.')
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
    def receive_price(self,key):
        print(f' Цена товара:',{self.items.values()})
        return self.items.get(key, None)

# метод для обновления цены товара.
    def update_price(self,key,new_price):
        if key in self.items:
            self.items[key] = new_price
        else:
            print(f'Товар "{key}" не найден.')

# Создаем несколько объектов класса `Store`:

store1 = Store("Булочная", "г. Москва ул. Тверская д.7")
store1.add_items ('батон', 10)
store1.add_items('бублик',5)

store2 = Store("Фрукты и овощи", "г. Владимир ул. Нижняя д.10")
store2.add_items('яблоки', 100)
store2.add_items('бананы', 70)
store2.add_items('лимоны', 120)
store2.add_items('помидоры', 200)

store3 = Store("Бакалея", "г. Санкт-Петербург ул. Кима д.4")
store3.add_items('мука', 50)
store3.add_items('чай', 10)

print(store2.name)
print(store2.adress)
print(store2.items)

store2.add_items('свекла', 20)
print(store2.items)

store2.receive_price('яблоки')
store2.update_price('яблоки',110)
print(store2.items)

store2.delete_item('яблоки')
print(store2.items)

# Методы работы со словарями:
# get(key[, default]): Возвращает значение для ключа kеу; если ключ не найден, возвращает default;
# items(): Возвращает пары (ключ, значение);
# keys(): Возвращает ключи в словаре;
# values(): Возвращает значения в словаре;
# pop(key[, default]): Удаляет элемент с ключом kеу и возвращает его значение;
# popitem(): Удаляет и возвращает пару (ключ, значение) из словаря;
# update([other]): Обновляет словарь элементами из other, перезаписывая существующие ключи.

