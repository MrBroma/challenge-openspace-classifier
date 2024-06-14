from typing import List
from utils.table import Table
from random import randrange
import pandas as pd


class Openspace:

    def __init__(self, setup: int = 6) -> None:
        self.number_of_tables = setup
        self.tables = [Table() for x in range(setup)]
        self.room_small = False
        pass

    def __str__(self) -> str:
        return f"Openspace representation with {self.number_of_tables} tables of {len(self.tables[0].seats)}"


    def organize(self,names: List[str]) -> None:
        """
        Function that will arrange the openspace with the names given in param.

        :param names List[str]: A list if str with the names to be organized.
        """

        n_peoples = len(names)
        n_tables = n_peoples // 4
        if n_peoples % 4 != 0:
            n_tables += 1
        if n_tables > self.number_of_tables:
            self.room_small = True
            return print("Not enough seats")
        effective_tables = self.tables[:n_tables]   #Reduce the usable tables to the minimum required to seat everyone, to avoid having people alone
        for i in range(n_peoples):
            new = names[randrange(len(names))]
            names.remove(new)

            effective_tables[i%n_tables].assign_seat(new)   #Using a modulo in the counter to cycle between tables

        pass

    def display(self) -> None:
        """Display the current arrangement of tables and colleagues"""
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
        elif self.room_small == False:
            return print("\nAll the tables are full.")


    def store(self,filename) -> None:
        """Store the current arrangement of tables in a CSV file

        :param filename str: The name of the file, whitout the extension"""

        l_table = []
        l_occupant = []
        for n, i in enumerate(self.tables):
            for j in i.seats:
                l_table.append(n + 1)
                l_occupant.append(j.occupant)
        df = pd.DataFrame(
            list(zip(l_table, l_occupant)), columns=["Table", "Colleague"]
        )
        df.to_csv(filename + ".csv")
        pass
