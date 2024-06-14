class Seat:

    def __init__(self, free: bool = True, occupant: str = "") -> None:
        self.free = free
        self.occupant = occupant

    def __str__(self) -> str:
        return f"Seat(free={self.free}, occupant='{self.occupant}')"

    def __repr__(self) -> str:
        return Seat()

    def set_occupant(self, name: str) -> bool:
        """
        Function that will allow to set a occupant to a seat if it's free ( in pramas)

        param free : A bool that will say if the seat is free or not.
        param occupant : a str that will put someone on the seat.
        return : A bool that will say if the seat is free or not.
        """
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

    """ this function is used to see if somone is one a seat ans if it is removes it to bring the seat back to free the"""


class Table:
    def __init__(self, capacity: int = 4) -> None:
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def __str__(self) -> str:
        seats_str = ", ".join(str(seat) for seat in self.seats)
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
