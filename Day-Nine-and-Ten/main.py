import requests
from flask import Flask, render_template, request
from scrapping import extract_story, extract_comments, extract_header_info

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"



# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route('/')
def index():
  order_by = request.args.get('order_by')
  if order_by == 'new':
    fromDB = db.get("new")
    if fromDB:
      stories = fromDB
    else:
      stories = extract_story(new)
      db["new"] = stories
  else :
    fromDB = db.get("popular")
    if fromDB:
      stories = fromDB
    else:
      stories = extract_story(popular)
      db["popular"] = stories
  return render_template("index.html",stories = stories,order_by = order_by)


@app.route('/<int:id>')
def detail(id):
  comments = extract_comments(id)
  header_info = extract_header_info(id)
  return render_template("detail.html",comments=comments,header_info=header_info)



app.run(host="0.0.0.0")