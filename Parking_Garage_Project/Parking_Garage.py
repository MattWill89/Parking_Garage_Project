class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            if not self.current_ticket:
                self.current_ticket = {"ticket_number": ticket_number, "parking_space": parking_space, "paid": False}
                print(f"Ticket {ticket_number} issued. Park in space {parking_space}.")
            else:
                print("You already have a ticket. Please pay or leave.")

    def pay_for_parking(self):
        if not self.current_ticket:
            print("No ticket. Please take a ticket first.")
            return

        if not self.current_ticket["paid"]:
            try:
                amount_paid = float(input("Enter the amount to pay: "))
                if amount_paid > 0:
                    print(f"Ticket {self.current_ticket['ticket_number']} has been paid. You have 15 minutes to leave.")
                    self.current_ticket["paid"] = True
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("You have already paid for parking.")

    def leave_garage(self):
        if not self.current_ticket:
            print("No ticket. Please take a ticket first.")
            return

        if self.current_ticket["paid"]:
            print("Thank you, have a nice day!")
            self.parking_spaces.append(self.current_ticket["parking_space"])
            self.tickets.append(self.current_ticket["ticket_number"])
            self.current_ticket = {}
        else:
            self.pay_for_parking()
            self.leave_garage()

garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

while True:
    action = input("What would you like to do? (Take a Ticket/Pay For Parking/Leave the Garage/Quit): ").lower()

    if action == "take a ticket":
        garage.take_ticket()
    elif action == "pay for parking":
        garage.pay_for_parking()
    elif action == "leave the garage":
        garage.leave_garage()
    elif action == "quit":
        break
    else:
        print("Invalid input. Please enter a valid action.")
