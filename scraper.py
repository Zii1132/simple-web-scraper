import requests
from bs4 import BeautifulSoup
import csv

# URL yang akan di-scrape
url = 'https://news.ycombinator.com/'

# Mengirimkan request ke halaman
response = requests.get(url)

# Mengecek apakah request berhasil
if response.status_code == 200:
    # Parse konten HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mencari semua judul artikel dengan tag <a>
    titles = soup.find_all('a', class_='storylink')

    # Menyimpan judul artikel dalam list
    articles = []
    for title in titles:
        articles.append(title.get_text())

    # Menyimpan artikel dalam file CSV
    with open('articles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])  # Header
        for article in articles:
            writer.writerow([article])

    print("Scraping completed! Data has been saved to articles.csv.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
