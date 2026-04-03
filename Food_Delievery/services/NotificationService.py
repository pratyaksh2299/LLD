from models.Order import Order

class NotificationService:
    def notify(self,order:Order):
        print(f"Notifying user {order.getUser().get_name()} about order {order.getorderId()} with total {order.total}")
        print(f"Scheduled time is {order.scheduled_time}")
