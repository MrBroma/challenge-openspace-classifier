from utils.openspace import Openspace
import pandas as pd

# Create a dataframe of Colleagues
colla_df = pd.read_excel(r"collab.xlsx")
# Create a list of Colleagues
colleagues_name = list(colla_df["Colleagues"])

# Openspace class initialization

classe = Openspace()
classe.organize(colleagues_name)
classe.display()

classe.store("arrangement")

