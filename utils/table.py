#class seat creation
class Seat:
    occupant =""
    free = True
    def __init__(self,free,occupant):
        self.free = free
        self.occupant = occupant
    
    def __str__(self) -> str:
        return f"TO DO"
    
#creation of the function st_occupant() chich will allow to set a person on a chair
    def set_occupant(free, occupant):
        if free == True:
            occupant = name
            free = False
            return occupant
    
    def remove_occupant(self,free, occupant):
        if occupant == name:
            occupant == ""
            free == True
            print(name)
            return name
        pass

# class Table --> manage the capacity and seats
class Table:
    capacity = 0
    seats = 2

    def __init__(self, capacity, seats) -> None:
        self.capacity = capacity
        self.seats = seats
        
    def __str__(self) -> str:
        return f"TO DO"

    def has_free_spot(self, capacity):
        if capacity != 0:
            print("There is free seats")
            return True
        pass

    def assign_seat(self, name):
        return name
        pass

    def left_capacity():
        return number_seats
        pass

