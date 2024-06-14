from utils.openspace import Openspace
import pandas as pd

# Create a dataframe of Colleagues
colla_df = pd.read_excel(r"collab.xlsx")
# Create a list of Colleagues
colleagues_name = list(colla_df['Colleagues'])

print(colleagues_name)

# Testing of Opensdpace class
test_names = ["Luffy","Ace","Sabo","Crocodile","Dragon","Garp","Kizaru","Ussop","Chopper","Franky","Brooks","Nami","Robbin"]

classe = Openspace(4)
classe.organize(test_names)
classe.display()