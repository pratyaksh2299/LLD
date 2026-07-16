from ParkingLot.models.Ticket import Ticket
class ParkingTicketManager:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self,vehicle,parking_spot):
        ticket = Ticket(vehicle,parking_spot)
        self.tickets[ticket.get_ticket_number()] = ticket
        return ticket
    
    def close_ticket(self,ticket_number):
        if ticket_number not in self.tickets:
            raise ValueError(f"Ticket number {ticket_number} not found")
        
        ticket = self.tickets[ticket_number]
        ticket.close_ticket()
        return ticket
    
    def get_ticket(self,ticket_number):
        if ticket_number not in self.tickets:
            raise ValueError(f"Ticket number {ticket_number} not found")
        
        return self.tickets[ticket_number]
