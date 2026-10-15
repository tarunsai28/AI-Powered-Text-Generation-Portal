
import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Website URL
url = "https://www.scrapethissite.com/pages/simple/"

# Step 2: Fetch website HTML
response = requests.get(url, timeout=30)
response.raise_for_status()

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all countries
countries = soup.find_all("div", class_="country")

# Step 5: Create CSV file
with open("countries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Capital", "Population", "Area"])

    for country in countries:
        name = country.find("h3", class_="country-name").get_text(strip=True)
        capital = country.find("span", class_="country-capital").get_text(strip=True)
        population = country.find("span", class_="country-population").get_text(strip=True)
        area = country.find("span", class_="country-area").get_text(strip=True)

        writer.writerow([name, capital, population, area])

print(f"Successfully scraped {len(countries)} countries!")
print("Data saved to countries.csv")
