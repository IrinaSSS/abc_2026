# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# ---------- Класс "Товар" (из задачи 37) ----------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value if value >= 0 else 0


# ---------- Класс "Заказ" (задача 38) ----------
class Order:
    def __init__(self):
        self.products = []          # список экземпляров Product

    def add_product(self, product):
        """Добавить товар в заказ."""
        self.products.append(product)

    def remove_product(self, product):
        """Удалить одно вхождение товара, если он есть в заказе."""
        if product in self.products:
            self.products.remove(product)

    @property
    def total_price(self):
        """Вычисляемая стоимость заказа — сумма текущих цен товаров."""
        return sum(product.price for product in self.products)


# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12