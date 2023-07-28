class Order:
	def __init__(self, product, customer,
				 price, date):
		self.product = product
		self.customer = customer
		self.price = price
		self.date = date

	def serialize(self):
		return {
			'product': self.product,
			'customer': self.customer,
			'price': self.price,
			'date': self.date
		}

def deserializer(order):
	return Order(
		product=order['product'],
		customer=order['customer'],
		price=order['price'],
		date=order['date']
	)

order = Order('Apple', 'Stella', 5.5,
			  '2023-02-14')
order_serializerd = order.serialize()
print(order_serializerd)
deserializer_order = deserializer(
	order_serializerd)
print(deserializer_order)