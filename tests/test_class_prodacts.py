from data.class_products import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
all = []
pay_rate = 1


def test_init():
  assert item1.categories == "Смартфон"
  assert item1.price == 10000
  assert item1.quantity == 20
  # Item.all.append(Item)


def test_calculate_total_price():
  assert item1.calculate_total_price() == item1.price * item1.quantity
  assert item2.calculate_total_price() == item2.price * item2.quantity


def test_apply_discount():
  discount_price = item1.price * item1.pay_rate
  item1.apply_discount()
  assert item1.price == discount_price
