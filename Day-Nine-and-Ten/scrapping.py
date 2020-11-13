import requests
import os

os.system("clear")

def extract_story(URL):
  results = requests.get(URL).json()["hits"]
  stories = []
  for result in results:
    title = result["title"]
    objectID = "/" + str(result["objectID"])
    url = result["url"]
    points = str(result["points"]) + " points"
    author = "By: " + result["author"]
    num_comments = str(result["num_comments"]) + " comments"
    stories.append({"title":title,"objectID":objectID,"url":url,"points":points,"author":author,"num_comments":num_comments})
  return stories


def extract_comments(id):
  URL = f"https://hn.algolia.com/api/v1/search?tags=comment,story_{id}"
  results = requests.get(URL).json()["hits"]
  comments = []
  for result in results:
    author = result["author"]
    comment_text = result["comment_text"]
    comments.append({"author":author,"comment_text":comment_text})
  return comments

def extract_header_info(id):
  URL = f"https://hn.algolia.com/api/v1/search?tags=story,story_{id}"
  result = requests.get(URL).json()["hits"]
  title = result[0]["title"]
  points = str(result[0]["points"]) + " points"
  author = "By "+result[0]["author"]
  url = result[0]["url"]
  return {"title":title, "points" : points, "author":author, "url":url}
