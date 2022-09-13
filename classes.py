class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            self.passengers.append(name)
            return False
        self.passengers.append(name)

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people: 
    if flight.add_passenger(person): 
        print(f"Added {person} to flight successfully.")
    else: 
        print(f"No available seats to add {person}")