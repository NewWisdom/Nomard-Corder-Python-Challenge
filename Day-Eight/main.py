import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def extract_ul():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text,"html.parser")
  super_brand = soup.find("div",{"id":"MainSuperBrand"})
  urls = super_brand.find_all("a",{"class":"goodsBox-info"})
  for a in urls:
    url = a.attrs["href"]
    company = a.find("span",{"class":"company"}).text
    infos = extract_info(url)
    save_to_csv(company,infos)


def extract_info(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  trs = soup.find("div",{"id":"NormalInfo"}).find("table").find("tbody").find_all("tr")
  infos = []
  for tr in trs:
    try:
      place = tr.find("td").text
      title = tr.find("span",{"class":"company"}).text
      work_time = tr.find("span",{"class":"time"}).text
      pay = tr.find("td",{"class":"pay"}).text
      upload_date = tr.find("td",{"class":"regDate last"}).text
      infos.append({'place':place, 'title':title,'time':work_time,"pay":pay,"date":upload_date})
    except:
      pass
  return infos

def save_to_csv(company,infos):
  file = open(company+".csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for info in infos:
    writer.writerow(list(info.values()))
  return


extract_ul()
