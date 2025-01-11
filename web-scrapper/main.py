import csv
import requests
from bs4 import BeautifulSoup


def scrape_website():
    url = input("Enter the website URL to scrape: ").strip()
    website_name = url.split("//")[-1].split("/")[0].replace("www.", "")
    output_file = f"{website_name}_data.csv"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    with open(output_file, 'w', newline='', encoding='utf-8') as file:  # Specify encoding
        writer = csv.writer(file)
        writer.writerow(["Tag", "Content"])  # Optional: Add a header row
        for tag in soup.find_all():
            if tag.text.strip():
                writer.writerow([tag.name, tag.text.strip()])


if __name__ == '__main__':
    scrape_website()
