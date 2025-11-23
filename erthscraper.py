#Script that scrapes recorded earthquakes of the the month by PHILVOLCS
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://earthquake.phivolcs.dost.gov.ph/"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

# Find all tbody elements
tbodies = soup.find_all("tbody")
#Philvolcs page data starts at the secod tbody 
second_tbody = tbodies[2]  

data_rows = []
for tr in second_tbody.find_all("tr"):
    cells = [cell.get_text(strip=True) for cell in tr.find_all("td")]
    #Only includes rows that exactly have 6 columns
    if len(cells) == 6:
        data_rows.append(cells)
#Define columns to match data
columns = ["DateTime", "Latitude", "Longitude", "Depth", "Magnitude", "Location"]

df = pd.DataFrame(data_rows, columns=columns)
# Display the extracted earthquake data in the console
print(df)
# Save the DataFrame to a CSV file
df.to_csv("earthquakes.csv", index=False, encoding="utf-8")