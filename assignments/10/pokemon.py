import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://pokemondb.net/pokedex/all"

# Step 1: Send an HTTP GET request to fetch the page
response = requests.get(url)
response.raise_for_status()  # Raises an error if the request was not successful

# Step 2: Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Locate the table by its ID
table = soup.find("table", {"id": "pokedex"})

# Step 4: Extract headers from the table
headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

# Step 5: Extract each row of data
rows = []
for tr in table.find("tbody").find_all("tr"):
    # Each cell in the row
    tds = tr.find_all("td")
    
    # Get the text from each cell
    row = [td.get_text(strip=True) for td in tds]
    rows.append(row)

# Step 6: Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Show the first few rows
print(df.head())

# Make a copy to keep the original df intact
df_clean = df.copy()

# If 'Type' column has multiple types separated by space (e.g. "Grass Poison"), split them:
df_clean['Type'] = df_clean['Type'].str.split(r'(?<!^)(?=[A-Z])')

# "Explode" the list of types so that each row contains exactly one type
df_exploded = df_clean.explode('Type').reset_index(drop=True)

# df_exploded will have one row per Pokemon per Type
# e.g. Bulbasaur will appear in two rows: one for "Grass" and one for "Poison".

# Group by 'Type' and find the Pokémon with the maximum Total in each group
strongest_by_type = (
    df_exploded.groupby('Type', as_index=False)
    .apply(lambda g: g.loc[g['Total'].idxmax()])
    .reset_index(drop=True)
)

# Let's see some results
strongest_by_type_sorted = strongest_by_type.sort_values(by='Total', ascending=False)
print(strongest_by_type[['Type', 'Name', 'Total']])

# Group by 'Type' and find the Pokémon with the maximum Attack in each group
best_attackers_by_type = (
    df_exploded.groupby('Type', as_index=False)
    .apply(lambda g: g.loc[g['Attack'].idxmax()])
    .reset_index(drop=True)
)

# Display the results
print(best_attackers_by_type[['Type', 'Name', 'Attack']])