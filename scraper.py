print("🚀 WEBS CRAPER MULAI!")
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "http://quotes.toscrape.com"
print(f"📡 Mengambil {url}...")

response = requests.get(url)
print(f"✅ HTTP {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

print(f"📚 {len(quotes)} quotes ditemukan!")

data = []
for i, quote in enumerate(quotes[:10], 1):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    data.append({"no": i, "quote": text, "author": author})

# SIMPAN JSON
with open('quotes.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n🎉 SUKSES! {len(data)} quotes → quotes.json")
print("Cek file: quotes.json")