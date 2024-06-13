from typing import List
from table import Table
from random import randrange


class Openspace:
    """TO DO : Write the docstring"""

    def __init__(self,setup:int = 6) -> None:
        self.number_of_tables = setup
        self.tables = [Table for x in range(setup)]
        pass

    def __str__(self) -> str:
        return f"TO DO"
    
    def organize(self,names: List[str]) -> None:
        for i in range(len(names)):
            new = names[randrange(len(names))]
            for table in self.tables:
                if table.has_free_spot == False:
                    continue
                else:
                    table.assign_seat(new)
            names.remove(new)
        pass
    
    def display(self) -> None:
        for i in range(len(self.number_of_tables)):
            table = self.tables[i]
            occupancy = table.capacity - table.left_capacity()
            print(f"Table {i+1} has {occupancy} seats taken :")
            for j in table.seats:
                print(f"{j.occupant}")
        pass

    def store(self,filename) -> None:
        pass

# Testing of Opensdpace class
test_names = ["Luffy","Ace","Sabo","Crocodile","Dragon","Garp","Kizaru","Ussop"]

classe = Openspace(3)
classe.organize(test_names)
classe.display()