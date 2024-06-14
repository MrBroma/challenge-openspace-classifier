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
        seats_str = ", ".join(str(seat) for seat in self.seats)
        return f"Table with {self.capacity} seats: [{seats_str}]"

    def __repr__(self) -> str:
        seats_str = ", ".join(str(seat) for seat in self.seats)
        return f"Table with {self.capacity} seats: [{seats_str}]"

    def has_free_spot(self) -> bool:
        """_summary_
        Function that will verify the presence of a free spot

        Returns:
            bool: True if a seat is free
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """_summary_
        FUnction to assign a person to a seat

        Args:
            name (str): name of the person (collaborator) who will be assign to a seat
            if a seat is free

        Returns:
            bool: True if a seat has bean assign to a person
        """
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def left_capacity(self) -> int:
        """_summary_
        Function to evaluate the left capacity

        Returns:
            int: return the left capacity
        """
        return sum(1 for seat in self.seats if seat.free)

