import csv
import requests
from bs4 import BeautifulSoup

def scrapedata(url):
    
    response = requests.get(url, timeout=10)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find_all('table')[0]
    
    rows = table.select('tbody > tr')
    
    with open ('coronavirus_worldometer.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(["Country,Other", "Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","Active Cases","Serious,Critical","Total Cases/1M Population","Deaths/1M Population","Total Tests","Tests/1M Population"])
        
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)
            
if __name__ == "__main__":
    url = "https://www.worldometers.info/coronavirus/"
    scrapedata(url)
    