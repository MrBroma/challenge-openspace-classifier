from typing import List
from table import Table
from random import randrange

class Openspace:
    """TO DO : Write the docstring"""

    def __init__(self,setup:int = 6) -> None:
        self.number_of_tables = setup
        self.tables = [Table() for x in range(setup)]
        pass

    def __str__(self) -> str:
        return f"TO DO"
    
    # def organize(self,names: List[str]) -> None:
    #     for i in range(len(names)):
    #         new = names[randrange(len(names))]
    #         for table in self.tables:
    #             if table.has_free_spot == False:
    #                 continue
    #             else:
    #                 table.assign_seat(new)
    #         names.remove(new)
    #     pass

    def organize(self,names: List[str]) -> None:
        n_peoples = len(names)
        n_tables = n_peoples // 4
        if n_peoples % 4 != 0:
            n_tables += 1
        if n_tables > self.number_of_tables:
            return "Not enough seats"
        effective_tables = self.tables[:n_tables]
        for i in range(n_peoples):
            new = names[randrange(n_peoples)]
            names.remove(new)
            effective_tables[i%n_tables].assign_seat()
        pass
    
    def display(self) -> None:
        for i in range(self.number_of_tables):
            table = self.tables[i]
            occupancy = table.capacity - table.left_capacity()
            if occupancy != 0:
                print(f"Table {i+1} has {occupancy} seats taken :")
                for j in table.seats:
                    if not j.free:
                        print(f" ┕{j.occupant}")
        pass

    def store(self,filename) -> None:
        pass

# Testing of Opensdpace class
test_names = ["Luffy","Ace","Sabo","Crocodile","Dragon","Garp","Kizaru","Ussop","Chopper"]

classe = Openspace(2)
classe.organize(test_names)
classe.display()