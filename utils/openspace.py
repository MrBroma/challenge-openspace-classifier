from typing import List
from utils.table import Table
from random import randrange
import pandas as pd

class Openspace:
    """TO DO : Write the docstring"""

    def __init__(self,setup:int = 6) -> None:
        self.number_of_tables = setup
        self.tables = [Table() for x in range(setup)]
        self.room_small = False
        pass

    def __str__(self) -> str:
        return f"TO DO"

    def organize(self,names: List[str]) -> None:
        n_peoples = len(names)
        n_tables = n_peoples // 4
        if n_peoples % 4 != 0:
            n_tables += 1
        if n_tables > self.number_of_tables:
            self.room_small = True
            return print("Not enough seats")
        effective_tables = self.tables[:n_tables]
        for i in range(n_peoples):
            new = names[randrange(len(names))]
            names.remove(new)
            effective_tables[i%n_tables].assign_seat(new)
        pass
    
    def display(self) -> None:
        free_seats = 0
        for i in range(self.number_of_tables):
            table = self.tables[i]
            occupancy = table.capacity - table.left_capacity()
            free_seats += table.left_capacity()
            if occupancy != 0:
                print(f"Table {i+1} has {occupancy} seats taken :")
                for j in table.seats:
                    if not j.free:
                        print(f" ├─ {j.occupant}")
        if free_seats != 0 and self.room_small == False:
            return print(f"\nThere is still {free_seats} free seats in the room.")
        else:
            return print("\nAll the tables are full.")

    def store(self,filename) -> None:
        l_table = []
        l_occupant = []
        for n,i in enumerate(self.tables):
            for j in i.seats:
                l_table.append(n+1)
                l_occupant.append(j.occupant)
        df = pd.DataFrame(list(zip(l_table,l_occupant)),columns=["Table","Colleague"])
        df.to_csv(filename + ".csv")
        pass

