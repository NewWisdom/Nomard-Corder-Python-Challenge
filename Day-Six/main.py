import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
url = "https://www.iban.com/currency-codes"

print("Welcom to CurrencyConvert Pro 2000\n")
countries = []
codes = []
cnt =0
def extract_countries_and_codes():
  global cnt
  result = requests.get(url)
  soup = BeautifulSoup(result.text,'html.parser')

  table = soup.find("table",{"class":"table table-bordered downloads tablesorter"})

  tbody = table.find('tbody')

  trs = tbody.find_all('tr')


  for idx, tr in enumerate(trs):
    tds = tr.find_all('td')
    if tds[1].text == "No universal currency":
      continue
    countries.append(tds[0].text)
    codes.append(tds[2].text)
    print(f"# {cnt} {countries[cnt]}")
    cnt+=1

def input_num1():
  try:
    num1 = int(input("\nWhere are you from? Choose a country by number.\n\n#:"))
    if num1 > cnt:
      print("Choose a number from list.")
      input_num1()
    else:
      con1 = countries[num1]
      print(f"{con1}\n")
      return codes[num1]
  except:
    print("That wasn't a number.")
    input_num1()

def input_num2():
  try:
    num2 = int(input("Now choose another country.\n\n#:"))
    if num2 > cnt:
      print("Choose a number from list.")
      input_num2()
    else:
      con2=countries[num2]
      print(f"{con2}\n")
      return codes[num2]
  except:
    print("That wasn't a number.")
    input_num2()
  
def how_many(code2):
  try:
      amount = int(input(f"How many COP do you want to convert to {code2}?\n"))
      return amount
  except:
    print("That wasn't a number.")
    how_many()

def get_result():
  global amount
  result = requests.get(f"https://transferwise.com/gb/currency-converter/{code1}-to-{code2}-rate?amount={amount}")
  soup = BeautifulSoup(result.text,"html.parser")
  h3 = soup.find("h3",{"class":"cc__source-to-target"})
  exchange_rate = h3.find("span",{"class":"text-success"}).text
  amount = int(amount)*float(exchange_rate)
  print(f"{code1}{format(amount,',')} is {format_currency(amount, code2, locale='ko_KR')}")
  
  

extract_countries_and_codes()
code1 = input_num1()
code2 = input_num2()
amount = how_many(code2)

get_result()

