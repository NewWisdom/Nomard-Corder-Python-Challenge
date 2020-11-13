import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

def input_num():
  try:
    num = int(input("#: "))
    if num > cnt:
      print("Choose a number from list.")
      input_num()
    else:
      print(f"You choose {countries[num]}\nThe currency code is {codes[num]}")
  except:
    print("That wasn't a number.")
    input_num()
  
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:\n")

result = requests.get(url)
soup = BeautifulSoup(result.text,'html.parser')

table = soup.find("table",{"class":"table table-bordered downloads tablesorter"})

tbody = table.find('tbody')

trs = tbody.find_all('tr')

countries = []
codes = []
cnt =0
for idx, tr in enumerate(trs):
  tds = tr.find_all('td')
  if tds[1].text == "No universal currency":
    continue
  countries.append(tds[0].text)
  codes.append(tds[2].text)
  print(f"# {cnt} {countries[cnt]}")
  cnt+=1
input_num()
