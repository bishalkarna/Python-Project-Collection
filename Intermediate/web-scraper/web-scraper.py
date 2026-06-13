import requests
from bs4 import BeautifulSoup
import csv

url = "https://risingnepaldaily.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h3")

    data = []

    for h in headlines:
        text = h.get_text().strip()
        if text:
            data.append([text])

    # Save to CSV
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])
        writer.writerows(data)

    print("Scraping completed! Saved to headlines.csv")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)