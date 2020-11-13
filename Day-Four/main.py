import requests
import os

def last_q():
  a = input("Do you want start over? y/n \n")
  return a

answer ='y'

while answer == 'y':
  os.system('clear')
  print("Wecome to isItDown.py!")
  s = input("Please write a URL or URLs you want to check. (separated by comma)\n")

  url_arr=s.split(",")
  url_arr = [e.strip() for e in url_arr]
  url_arr = [e if ("http://" or "https://") in url_arr else "http://"+str(e) for e in url_arr]

  for e in url_arr:
    try:
      r= requests.get(e)
      print(f"{e} is up!")
    except requests.ConnectionError:
      print(f"{e} is down!")


  answer = last_q()
  while answer != 'y' and answer !='n':
    print("That is not valid answer")
    answer = last_q()



