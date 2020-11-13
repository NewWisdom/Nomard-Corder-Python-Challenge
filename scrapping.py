"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import requests
from bs4 import BeautifulSoup

def extract_wwr(word):
  URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  result = requests.get(URL,allow_redirects=False)
  soup = BeautifulSoup(result.text,"html.parser")
  ul = soup.find("div",{"class":"content"}).find("div",{"class":"jobs-container"}).find("section",{"id":"category-2"}).find("article").find("ul")
  lis = ul.find_all("li",{"class":"feature"})
  jobs = []
  for li in lis:
    a= li.find_all("a")
    if len(a)>1:
      a[0]=a[1]
    title = a[0].find("span",{"class":"title"}).text
    company = a[0].find("span",{"class":"company"}).text
    href = "https://weworkremotely.com" + a[0].attrs["href"]
    jobs.append({"title":title,"company":company,"href":href})
  return jobs

def extract_stackoverflow(word):
  URL = f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = get_last_page(URL)
  jobs = []
  for i in range(last_page):
    URL+=f"&pg={i}"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    list_result = soup.find("div",{"class":"listResults"})
    divs = list_result.find_all("div",{"class":"grid--cell fl1"})
    for div in divs:
      a = div.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).find("a",{"class":"s-link stretched-link"})
      href = "https://stackoverflow.com" + a.attrs["href"]
      title = a.attrs["title"]
      company = div.find("h3",{"class":"fc-black-700 fs-body1 mb4"}).find("span").text
      jobs.append({"title":title,"company":company,"href":href})
  return jobs

def extract_remoteok(word):
  URL = f"https://remoteok.io/remote-{word}-jobs"
  result = requests.get(URL,allow_redirects=False)
  soup = BeautifulSoup(result.text,"html.parser")
  trs = soup.find_all("tr", {"class": "job"})
  jobs = []
  for tr in trs:
    td = tr.find("td",{"class":"company position company_and_position"})
    a = td.find("a",{"class":"preventLink"})
    href = "https://remoteok.io"+a.attrs["href"]
    title = a.find("h2").text
    company = td.find("a",{"class":"companyLink"}).find("h3").text
    jobs.append({"title":title,"company":company,"href":href})
  return jobs

def get_last_page(URL):
  result = requests.get(URL,allow_redirects=False)
  soup  = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div",{"class":"s-pagination"})

  links = pagination.find_all('a')
  return (len(links)-1)