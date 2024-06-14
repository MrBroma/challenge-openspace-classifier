class Seat:
    def __init__(self, free: bool = True, occupant: str = ""):
        self.free = free
        self.occupant = occupant
    
    def __str__(self) -> str:
        return f"Seat(free={self.free}, occupant='{self.occupant}')"
    
    def set_occupant(self, name: str) -> bool:
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False
    
    def remove_occupant(self) -> bool:
        if not self.free:
            self.occupant = ""
            self.free = True
            return True
        return False

class Table:
    def __init__(self, capacity: int = 4) -> None:
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def __str__(self) -> str:
        seats_str = ', '.join(str(seat) for seat in self.seats)
        return f"Table with {self.capacity} seats: [{seats_str}]"

    def has_free_spot(self) -> bool:
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name: str) -> bool:
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def left_capacity(self) -> int:
        return sum(1 for seat in self.seats if seat.free)

# Exemple d'utilisation
table = Table()
print(table)  # Affiche l'état initial de la table

if table.has_free_spot():
    table.assign_seat("Alice")
print(table)  # Affiche l'état de la table après l'assignation

if table.has_free_spot():
    table.assign_seat("Bob")
print(table)  # Affiche l'état de la table après une autre assignation
