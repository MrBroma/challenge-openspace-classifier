from typing import List
from table import Table


class Openspace:
    """TO DO : Write the docstring"""

    def __init__(self) -> None:
        self.tables = []
        self.number_of_tables = len(self.tables)
        pass

    def __str__(self) -> str:
        return f"TO DO"
    
    def organize(self,names) -> List:
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

