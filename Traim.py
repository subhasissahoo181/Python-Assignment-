# Write a class Train which has methods to book a ticket, get status[no of seats] and get fare information of trains remaining under Indian Ralway.

class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats


    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the ticket is:{self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats-1

        else:
            print("Sorry this train is full! Kindly try again")

    def cancelTicket(self, seatNo):
        pass



intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()