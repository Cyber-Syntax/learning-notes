from typing import TypedDict


class Item(TypedDict):
    category: str
    price: float


class Order:
    def __init__(self, customer: str, items: list[Item]):
        self.customer: str = customer
        self.items: list[Item] = items

    def tax(self, item: Item) -> float:
        if item["category"] == "electronics":
            return item["price"] * 0.15
        else:
            return item["price"] * 0.1

    def discount(self, item: Item) -> float:
        if item["price"] > 100:
            return item["price"] * 0.05
        return 0

    def print_order_summary(self, total: float) -> None:
        print(f"Customer: {self.customer}")
        print(f"Total: {total}")

    def save_order(self, total: float) -> None:
        with open("orders.txt", "a") as file:
            file.write(f"{self.customer}: {total}\n")

    def process_order(self) -> float:
        total = 0
        for item in self.items:
            tax_amount: float = self.tax(item)
            discount_amount: float = self.discount(item)
            item_total: float = item["price"] + tax_amount - discount_amount
            total += item_total
        self.print_order_summary(total)
        self.save_order(total)
        return total


order = Order(
    "John Doe",
    [{"category": "electronics", "price": 200}],
)
print(Order)
print(order)
print(order.process_order())


# Above code shows how to refactor a long method into smaller methods.
# This is bad written code below show long methods etc.
def process_order(order):
    total = 0
    for item in order["items"]:
        if item["category"] == "electronics":
            tax = item["price"] * 0.15
        else:
            tax = item["price"] * 0.1
        discount = 0
        if item["price"] > 100:
            discount = item["price"] * 0.05
        item_total = item["price"] + tax - discount
        total += item_total
    print(f"Customer: {order['customer']}")
    print(f"Total: {total}")
    with open("orders.txt", "a") as file:
        file.write(f"{order['customer']}: {total}\n")
