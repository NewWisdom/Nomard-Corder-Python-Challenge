import requests
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

def extract_subreddit(read_arr):
  reddits = []
  for interested in read_arr:
    URL = f"https://www.reddit.com/r/{interested}/top/?t=month"
    result = requests.get(URL,headers=headers)
    soup = BeautifulSoup(result.text,"html.parser")
    # div = soup.find("div",{"class":"rpBJOHq2PR60pnwJlUyP0"})
    divs = soup.find_all("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
    for div in divs:
      upvote = div.find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).text
      if upvote =='•':
        upvote = '0'
      href = div.find("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
      if href:
        href = href.attrs['href']
      title = div.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).text
      reddits.append({"title":title,"href":href,"upvote":upvote,"interested":interested})  
    reddits.sort(key= lambda x:x["upvote"],reverse = True)
    return reddits

  # for upvote in upvotes:
  #   if upvote.text == '•':
  #     pass
  #   else:
  #     print(upvote.text)
  # for a in ass:
  #   url = a["href"]
  #   print(url)
  
  
  