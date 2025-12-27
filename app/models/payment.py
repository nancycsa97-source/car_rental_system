class payment:
    def __init__(
        self, id, amount, status, order_id, user_id, payment_method, date, timestamp
    ):
        self.id = id
        self.amount = amount
        self.status = status
        self.order_id = order_id
        self.user_id = user_id
        self.payment_method = payment_method
        self.date = date
        self.timestamp = timestamp
        amount = 100
        print(f"we have received a payment of amount {self.amount}")
